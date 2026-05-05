import streamlit as st
import datetime

if not st.session_state.get("logged_in"):
    st.switch_page("app.py")

plants = st.session_state.get("plants", [])
dil    = st.session_state.get("dil", "🇹🇷 Türkçe")
TR     = dil == "🇹🇷 Türkçe"
DB     = st.session_state.get("db_aktif", False)

hava = None
try:
    from weather_service import hava_durumu_kontrol
    hava = hava_durumu_kontrol("Elazig")
except Exception:
    pass

st.title("📅 " + ("Bakım Takvimi" if TR else "Care Calendar"))
st.divider()

# done_tasks session'da yoksa DB'den yükle
if "done_tasks" not in st.session_state:
    if DB:
        try:
            from database_handler import tamamlanan_gorevleri_getir
            st.session_state.done_tasks = tamamlanan_gorevleri_getir()
        except Exception:
            st.session_state.done_tasks = set()
    else:
        st.session_state.done_tasks = set()

if hava and hava["yagmur_var_mi"]:
    st.warning("🌧️ " + ("Bugün yağmur var — dış mekân sulama görevleri otomatik atlandı." if TR else "Rain today — outdoor watering skipped."))

col_tarih, col_filtre = st.columns([1, 2])
with col_tarih:
    tarih = st.date_input("Tarih" if TR else "Date", datetime.date.today())
with col_filtre:
    filtre_sec = ["Tümü", "Sulama", "Gübre", "Kontrol", "Temizlik"] if TR else ["All", "Watering", "Fertilize", "Check", "Clean"]
    filtre     = st.selectbox("Görev Türü" if TR else "Task Type", filtre_sec)

st.divider()

IKONLAR = {"Sulama": "💧", "Gübre": "🌱", "Kontrol": "🔍", "Temizlik": "🍃",
           "Watering": "💧", "Fertilize": "🌱", "Check": "🔍", "Clean": "🍃"}
bugun   = datetime.date.today()
yagmur  = hava["yagmur_var_mi"] if hava else False

def gorev_olustur(plants, yagmur=False):
    gorevler = []
    for p in plants:
        dis_mekan  = p["konum"] in ["Balkon", "Bahçe", "Balcony", "Garden"]
        son_sulama = p.get("son_sulama")

        # Sulama tarihi hesapla
        if son_sulama:
            try:
                son  = datetime.date.fromisoformat(str(son_sulama)[:10])
                sulama_tarihi = son + datetime.timedelta(days=p["sulama_periyodu"])
            except Exception:
                sulama_tarihi = bugun
        else:
            sulama_tarihi = bugun  # Hiç sulanmamış → bugün

        # Yağmurluysa dış mekan sulama yapma
        if not (yagmur and dis_mekan):
            gorevler.append({
                "bitki":    p["ad"],
                "bitki_id": p["id"],
                "tur":      "Sulama" if TR else "Watering",
                "tarih":    sulama_tarihi,
                "not":      f"{'Her' if TR else 'Every'} {p['sulama_periyodu']} {'günde bir sulama' if TR else 'days watering'}"
            })

        gorevler.append({"bitki": p["ad"], "bitki_id": p["id"], "tur": "Temizlik" if TR else "Clean",
                         "tarih": bugun + datetime.timedelta(days=1),  "not": "Yaprak temizliği" if TR else "Leaf cleaning"})
        gorevler.append({"bitki": p["ad"], "bitki_id": p["id"], "tur": "Gübre" if TR else "Fertilize",
                         "tarih": bugun + datetime.timedelta(days=3),  "not": "Gübre zamanı" if TR else "Fertilize time"})
        gorevler.append({"bitki": p["ad"], "bitki_id": p["id"], "tur": "Kontrol" if TR else "Check",
                         "tarih": bugun + datetime.timedelta(days=7),  "not": "Genel sağlık kontrolü" if TR else "General health check"})
    return gorevler

tum_gorevler = gorev_olustur(plants, yagmur=yagmur)

# Filtrele
if filtre not in ["Tümü", "All"]:
    tum_gorevler = [g for g in tum_gorevler if g["tur"] == filtre]

gecmis   = [g for g in tum_gorevler if g["tarih"] < bugun]
bugunler = [g for g in tum_gorevler if g["tarih"] == bugun]
gelecek  = [g for g in tum_gorevler if g["tarih"] > bugun]

def gorev_listele(gorev_list, baslik):
    if not gorev_list:
        return
    st.subheader(baslik)
    for g in gorev_list:
        gid  = f"{g['bitki']}_{g['tur']}_{g['tarih']}"
        ikon = IKONLAR.get(g["tur"], "📌")
        tamamlandi = gid in st.session_state.done_tasks

        with st.container(border=True):
            c1, c2 = st.columns([5, 1])
            with c1:
                if tamamlandi:
                    st.markdown(f"~~{ikon} **{g['bitki']}** — {g['tur']}~~")
                else:
                    st.write(f"{ikon} **{g['bitki']}** — {g['tur']}")
                st.caption(f"{g['not']}  |  {g['tarih'].strftime('%d %b %Y')}")
            with c2:
                done = st.checkbox("✓", key=f"chk_{gid}", value=tamamlandi)
                if done and gid not in st.session_state.done_tasks:
                    st.session_state.done_tasks.add(gid)
                    # DB'ye kaydet
                    if DB:
                        try:
                            from database_handler import gorev_tamamla, sulama_kaydet, saglik_hesapla, bitki_guncelle
                            gorev_tamamla(gid)
                            # Sulama göreviyse sulamayı da kaydet
                            if g["tur"] in ["Sulama", "Watering"]:
                                bugun_str = str(bugun)
                                sulama_kaydet(g["bitki_id"], bugun_str)
                                yeni_saglik = saglik_hesapla(bugun_str, next((p["sulama_periyodu"] for p in plants if p["id"] == g["bitki_id"]), 7))
                                bitki_guncelle(g["bitki_id"], yeni_saglik=yeni_saglik, yeni_son_sulama=bugun_str)
                                # Session'u güncelle
                                for bp in st.session_state.plants:
                                    if bp["id"] == g["bitki_id"]:
                                        bp["son_sulama"] = bugun_str
                                        bp["saglik"]     = yeni_saglik
                                        break
                        except Exception as e:
                            print("Görev tamamlama hatası:", e)
                    st.rerun()

                elif not done and gid in st.session_state.done_tasks:
                    st.session_state.done_tasks.discard(gid)
                    if DB:
                        try:
                            from database_handler import gorev_tamamlanmadi
                            gorev_tamamlanmadi(gid)
                        except Exception:
                            pass
                    st.rerun()

gorev_listele(gecmis,   "🔴 " + ("Gecikmiş" if TR else "Overdue"))
gorev_listele(bugunler, "🟢 " + ("Bugün" if TR else "Today"))
gorev_listele(gelecek,  "🔵 " + ("Yaklaşan" if TR else "Upcoming"))

if not tum_gorevler:
    st.info("Bu filtre için görev bulunamadı." if TR else "No tasks for this filter.")

st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("Toplam Görev" if TR else "Total Tasks",     len(tum_gorevler))
c2.metric("Tamamlanan" if TR else "Completed",         len([g for g in tum_gorevler if f"{g['bitki']}_{g['tur']}_{g['tarih']}" in st.session_state.done_tasks]))
c3.metric("Bekleyen" if TR else "Pending",             len([g for g in tum_gorevler if f"{g['bitki']}_{g['tur']}_{g['tarih']}" not in st.session_state.done_tasks]))
