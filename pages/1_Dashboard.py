import streamlit as st
import datetime
from weather_service import hava_durumu_kontrol

if not st.session_state.get("logged_in"):
    st.switch_page("app.py")

plants = st.session_state.get("plants", [])
dil    = st.session_state.get("dil", "🇹🇷 Türkçe")
TR     = dil == "🇹🇷 Türkçe"
DB     = st.session_state.get("db_aktif", False)

hava = hava_durumu_kontrol("Elazig")

st.title("🌿 " + ("Panel" if TR else "Dashboard"))
st.caption(f"{len(plants)} {'Sağlıklı Bitki' if TR else 'Healthy Plants'}")
st.divider()

col_hava, col_bilgi = st.columns([1, 3])
with col_hava:
    if hava:
        st.metric("🌡️ " + ("Sıcaklık" if TR else "Temperature"), f"{hava['sicaklik']:.1f}°C", hava["durum"])
    else:
        st.metric("🌡️ " + ("Sıcaklık" if TR else "Temperature"), "—", "—")
with col_bilgi:
    if hava and hava.get("_mock"):
        st.warning("⚠️ " + ("Hava durumu API'sine ulaşılamadı." if TR else "Weather API unavailable."))
    elif hava and hava["yagmur_var_mi"]:
        st.warning("🌧️ " + ("Bugün yağmur var. Dış mekân bitkilerini sulamayın." if TR else "Rain today. Skip outdoor plants."))
    elif hava:
        st.info(f"☀️ {'Hava' if TR else 'Weather'}: {hava['durum']} — {hava['sicaklik']:.1f}°C")

st.divider()

avg_saglik = int(sum(p["saglik"] for p in plants) / len(plants)) if plants else 0
bugun      = datetime.date.today()

thirsty = []
for p in plants:
    son = p.get("son_sulama")
    if son:
        try:
            if (bugun - datetime.date.fromisoformat(str(son)[:10])).days >= p["sulama_periyodu"]:
                thirsty.append(p)
        except Exception:
            thirsty.append(p)
    else:
        thirsty.append(p)

m1, m2, m3 = st.columns(3)
m1.metric("SAĞLIK SKORU" if TR else "HEALTH SCORE", f"%{avg_saglik}")
m2.metric("BİTKİLER" if TR else "PLANTS",           str(len(plants)))
m3.metric("SULAMA BEKLEYEN" if TR else "NEED WATER", str(len(thirsty)))

st.divider()
sol, sag = st.columns([1, 1.6])

with sol:
    st.subheader("💧 " + ("Bugün Susayanlar" if TR else "Thirsty Today"))

    filtreli = thirsty
    if hava and hava["yagmur_var_mi"]:
        filtreli = [p for p in thirsty if p["konum"] not in ["Balkon", "Bahçe"]]
        if len(filtreli) < len(thirsty):
            st.caption("🌧️ " + ("Dış mekân bitkiler yağmur nedeniyle çıkarıldı." if TR else "Outdoor plants skipped due to rain."))

    if filtreli:
        for p in filtreli:
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write(f"🌿 **{p['ad']}**")
            with col_b:
                if st.button("✅", key=f"sulandi_{p['id']}", help="Sulandı" if TR else "Watered"):
                    bugun_str = str(bugun)
                    if DB:
                        try:
                            from database_handler import sulama_kaydet, bitki_guncelle
                            sulama_kaydet(p["id"], bugun_str)
                            # Sadece +10 can suyu ver, maksimum 100 olsun
                            yeni_saglik = min(100, p["saglik"] + 10) 
                            bitki_guncelle(p["id"], yeni_saglik=yeni_saglik, yeni_son_sulama=bugun_str)
                        except Exception as e:
                            print("Sulama hatası:", e)
                            yeni_saglik = min(100, p["saglik"] + 10)
                            
                    for bp in st.session_state.plants:
                        if bp["id"] == p["id"]:
                            bp["son_sulama"] = bugun_str
                            bp["saglik"] = yeni_saglik
                            break
                    # Görevi done_tasks'a ekle → takvimden de kaybolur
                    gorev_id = f"{p['ad']}_Sulama_{bugun}"
                    st.session_state.done_tasks.add(str(gorev_id))
                    st.toast(f"{'Sulandı' if TR else 'Watered'}: {p['ad']} 💧")
                    st.rerun()
    else:
        st.success("🎉 " + ("Bugün sulama gerekenler yok!" if TR else "No watering needed today!"))

    st.divider()
    st.info("🌱 " + ("**İpucu:** Bitkilerinizi sabah sulamak mantar oluşumunu engeller." if TR else "**Tip:** Water in the morning to prevent fungal growth."))

with sag:
    if plants:
        secilen = st.selectbox("🌿 " + ("Bitki seçin" if TR else "Select plant"), [p["ad"] for p in plants])
        p = next(x for x in plants if x["ad"] == secilen)

        st.subheader(f"🪴 {p['ad']}")
        st.caption(f"*{p['tur']}*")

        c1, c2, c3 = st.columns(3)
        loc_map = {"Salon": "Living Room", "Mutfak": "Kitchen", "Yatak Odası": "Bedroom", "Ofis": "Office", "Balkon": "Balcony", "Banyo": "Bathroom", "Bahçe": "Garden"}
        en_to_tr = {v: k for k, v in loc_map.items()}
        gosterilen_konum = en_to_tr.get(p["konum"], p["konum"]) if TR else loc_map.get(p["konum"], p["konum"])
        
        c1.metric("Konum" if TR else "Location", gosterilen_konum)
        c2.metric("Sulama" if TR else "Watering", f"{p['sulama_periyodu']}g" if TR else f"{p['sulama_periyodu']}d")
        isik_sozluk = {"Indirect sunlight": "Dolaylı Güneş", "Part shade": "Yarı Gölge", "Full sun": "Tam Güneş", "Bright indirect": "Parlak Dolaylı", "Unknown": "Bilinmiyor"}
        gosterilen_isik = isik_sozluk.get(p["isik"], p["isik"]) if TR else p["isik"]
        c3.metric("Işık" if TR else "Light", gosterilen_isik)

        st.write("**" + ("Sağlık Durumu" if TR else "Health Status") + "**")
        st.progress(p["saglik"] / 100)
        label = ("Çok Sağlıklı 💚" if TR else "Very Healthy 💚") if p["saglik"] >= 80 else \
                ("Orta 🟡" if TR else "Moderate 🟡") if p["saglik"] >= 50 else \
                ("Hasta 🔴" if TR else "Unhealthy 🔴")
        st.caption(f"%{p['saglik']} — {label}")

        if p.get("son_sulama"):
            st.caption(f"{'Son sulama' if TR else 'Last watered'}: {p['son_sulama']}")

        if st.button("📝 " + ("Not Ekle" if TR else "Add Note"), use_container_width=True):
            st.switch_page("pages/2_Bitki_Kutuphanesi.py")

st.divider()

st.subheader("🕐 " + ("Yaklaşan Görevler" if TR else "Upcoming Tasks"))
if plants:
    gosterilen = 0
    for p in plants:
        son = p.get("son_sulama")
        try:
            sonraki = datetime.date.fromisoformat(str(son)[:10]) + datetime.timedelta(days=p["sulama_periyodu"]) if son else bugun
        except Exception:
            sonraki = bugun

        # Sulandıysa gösterme
        gorev_id = f"{p['ad']}_Sulama_{sonraki}"
        if str(gorev_id) in st.session_state.done_tasks:
            continue

        gecikme = (bugun - sonraki).days if sonraki < bugun else 0
        ikon    = "🔴" if gecikme > 0 else "💧"
        g1, g2  = st.columns([3, 1])
        with g1:
            st.write(f"{ikon} **{p['ad']}** — {'Sulama' if TR else 'Water'}")
        with g2:
            st.caption(sonraki.strftime("%d %b"))
        gosterilen += 1

    if gosterilen == 0:
        st.success("🎉 " + ("Tüm görevler tamamlandı!" if TR else "All tasks completed!"))
else:
    st.info("Bitki ekleyin, görevler otomatik oluşsun." if TR else "Add plants to see tasks.")