import streamlit as st
import datetime

if not st.session_state.get("logged_in"):
    st.switch_page("app.py")

dil    = st.session_state.get("dil", "🇹🇷 Türkçe")
TR     = dil == "🇹🇷 Türkçe"
DB     = st.session_state.get("db_aktif", False)

st.title("📚 " + ("Bitki Kütüphanesi" if TR else "Plant Library"))
st.caption(f"{'Koleksiyonunuzda' if TR else 'You have'} {len(st.session_state.plants)} {'bitki var.' if TR else 'plants.'}")
st.divider()

tab_liste, tab_ekle, tab_notlar = st.tabs([
    "🌿 " + ("Koleksiyonum" if TR else "My Collection"),
    "➕ " + ("Yeni Bitki Ekle" if TR else "Add New Plant"),
    "📝 " + ("Notlar" if TR else "Notes"),
])

# ── TAB 1: Liste ──
with tab_liste:
    ara    = st.text_input("🔍 " + ("Bitki Ara" if TR else "Search Plant"), placeholder="İsim veya tür yazın..." if TR else "Enter name or species...")
    plants = st.session_state.plants
    if ara:
        plants = [p for p in plants if ara.lower() in p["ad"].lower() or ara.lower() in p["tur"].lower()]

    if not plants:
        st.info("Sonuç bulunamadı." if TR else "No results found.")
    else:
        sol, sag = st.columns(2)
        for i, p in enumerate(plants):
            with (sol if i % 2 == 0 else sag):
                if p["saglik"] >= 80:
                    saglik_label = "💚 Çok Sağlıklı" if TR else "💚 Very Healthy"
                elif p["saglik"] >= 50:
                    saglik_label = "🟡 Orta" if TR else "🟡 Moderate"
                else:
                    saglik_label = "🔴 Hasta" if TR else "🔴 Unhealthy"

                with st.container(border=True):
                    st.subheader(p["ad"])
                    st.caption(f"*{p['tur']}*")
                    c1, c2, c3 = st.columns(3)
                    loc_map = {"Salon": "Living Room", "Mutfak": "Kitchen", "Yatak Odası": "Bedroom", "Ofis": "Office", "Balkon": "Balcony", "Banyo": "Bathroom", "Bahçe": "Garden"}
                    en_to_tr = {v: k for k, v in loc_map.items()}
                    gosterilen_konum = en_to_tr.get(p["konum"], p["konum"]) if TR else loc_map.get(p["konum"], p["konum"])
                    
                    c1.metric("Konum" if TR else "Location", gosterilen_konum)
                    c2.metric("Sulama" if TR else "Watering", f"{p['sulama_periyodu']}g/bir" if TR else f"{p['sulama_periyodu']}d")
                    c3.metric("Sağlık" if TR else "Health",   f"%{p['saglik']}")
                    isik_sozluk = {"Indirect sunlight": "Dolaylı Güneş", "Part shade": "Yarı Gölge", "Full sun": "Tam Güneş", "Bright indirect": "Parlak Dolaylı", "Unknown": "Bilinmiyor"}
                    gosterilen_isik = isik_sozluk.get(p["isik"], p["isik"]) if TR else p["isik"]
                    st.write(f"☀️ {gosterilen_isik}  —  {saglik_label}")
                    if st.button("🗑️ " + ("Sil" if TR else "Delete"), key=f"sil_db_{p['id']}", use_container_width=True):
                        if DB:
                            try:
                                from database_handler import bitki_sil
                                bitki_sil(p["id"])
                            except Exception:
                                pass
                        st.session_state.plants = [b for b in st.session_state.plants if b["id"] != p["id"]]
                        st.rerun()

# ── TAB 2: Ekle ──
with tab_ekle:
    st.subheader("🌱 " + ("Yeni Bitki Ekle" if TR else "Add New Plant"))
    st.caption("Tür girilince sulama ve ışık bilgisi otomatik hesaplanır." if TR else "Watering and light info is auto-calculated from species.")

    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            yeni_ad    = st.text_input("Bitki Adı" if TR else "Plant Name",    placeholder="Barış Çiçeği" if TR else "Peace Lily")
            yeni_tur   = st.text_input("Tür (Latince)" if TR else "Species",   placeholder="Spathiphyllum")
            konum_sec  = ["Salon","Mutfak","Yatak Odası","Ofis","Balkon","Banyo","Bahçe"] if TR else ["Living Room","Kitchen","Bedroom","Office","Balcony","Bathroom","Garden"]
            yeni_konum = st.selectbox("Konum" if TR else "Location", konum_sec)
        with c2:
            yeni_tarih = st.date_input("Ekim Tarihi" if TR else "Planting Date", datetime.date.today())

        if st.button("🌿 " + ("Koleksiyona Ekle" if TR else "Add to Collection"), use_container_width=True):
            if yeni_ad and yeni_tur:
                with st.spinner("Bitki bilgisi alınıyor..." if TR else "Fetching plant info..."):
                    from perenual_service import bitki_bilgisi_getir
                    api_bilgileri = bitki_bilgisi_getir(yeni_tur)
                    sulama_gun    = api_bilgileri.get("periyot_gun", 7) if api_bilgileri else 7
                    isik_bilgisi  = api_bilgileri.get("isik", "Bilinmiyor") if api_bilgileri else "Unknown"

                if DB:
                    try:
                        from database_handler import akilli_bitki_ekle, tum_bitkileri_getir
                        akilli_bitki_ekle(ad=yeni_ad, tur=yeni_tur, ekim_tarihi=str(yeni_tarih), konum=yeni_konum, sulama_periyodu=sulama_gun)
                        rows = tum_bitkileri_getir()
                        if rows:
                            st.session_state.plants = [
                                {"id": r[0], "ad": r[1], "tur": r[2], "ekim_tarihi": r[3],
                                 "sulama_periyodu": r[4], "konum": r[5],
                                 "saglik": r[6] if r[6] else 80,
                                 "isik": isik_bilgisi if r[1] == yeni_ad else "Bilinmiyor",
                                 "son_sulama": str(r[7]) if r[7] else None}
                                for r in rows
                            ]
                        st.success(f"✅ **{yeni_ad}** {'veritabanına eklendi!' if TR else 'added to database!'}")
                    except Exception as e:
                        st.error(f"DB hatası: {e}")
                        _id = max((p["id"] for p in st.session_state.plants), default=0) + 1
                        st.session_state.plants.append({"id": _id, "ad": yeni_ad, "tur": yeni_tur,
                            "ekim_tarihi": str(yeni_tarih), "sulama_periyodu": sulama_gun,
                            "konum": yeni_konum, "saglik": 80, "isik": isik_bilgisi, "son_sulama": None})
                        st.success(f"✅ **{yeni_ad}** {'oturuma eklendi.' if TR else 'added to session.'}")
                else:
                    _id = max((p["id"] for p in st.session_state.plants), default=0) + 1
                    st.session_state.plants.append({"id": _id, "ad": yeni_ad, "tur": yeni_tur,
                        "ekim_tarihi": str(yeni_tarih), "sulama_periyodu": sulama_gun,
                        "konum": yeni_konum, "saglik": 80, "isik": isik_bilgisi, "son_sulama": None})
                    st.success(f"✅ **{yeni_ad}** {'oturuma eklendi.' if TR else 'added to session.'}")
                st.rerun()
            else:
                st.error("Bitki adı ve türü zorunlu." if TR else "Plant name and species are required.")

# ── TAB 3: Notlar ──
with tab_notlar:
    st.subheader("📝 " + ("Bitki Notları" if TR else "Plant Notes"))

    if not st.session_state.plants:
        st.info("Önce bir bitki ekleyin." if TR else "Add a plant first.")
    else:
        secilen_bitki = st.selectbox("Bitki seçin" if TR else "Select plant",
                                      [p["ad"] for p in st.session_state.plants], key="not_bitki_sec")
        secilen_p = next(p for p in st.session_state.plants if p["ad"] == secilen_bitki)

        if "notlar" not in st.session_state:
            st.session_state.notlar = {}

        bitki_notlar = st.session_state.notlar.get(secilen_p["id"], [])

        if bitki_notlar:
            for n in reversed(bitki_notlar):
                with st.container(border=True):
                    st.caption(n["tarih"])
                    st.write(n["icerik"])
        else:
            st.info("Bu bitki için henüz not yok." if TR else "No notes for this plant yet.")

        st.divider()
        yeni_not = st.text_area("Yeni not" if TR else "New note",
                                 placeholder="Yapraklarda sararma görüldü..." if TR else "Noticed yellowing leaves...")
        if st.button("💾 " + ("Notu Kaydet" if TR else "Save Note"), use_container_width=True):
            if yeni_not.strip():
                st.session_state.notlar.setdefault(secilen_p["id"], []).append({
                    "icerik": yeni_not.strip(), "tarih": str(datetime.date.today())
                })
                st.success("Not kaydedildi!" if TR else "Note saved!")
                st.rerun()
            else:
                st.error("Not boş olamaz." if TR else "Note cannot be empty.")