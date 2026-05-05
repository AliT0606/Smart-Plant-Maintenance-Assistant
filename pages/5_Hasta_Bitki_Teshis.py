import streamlit as st
from perenual_service import hastalik_tespit

if not st.session_state.get("logged_in"):
    st.switch_page("app.py")

dil = st.session_state.get("dil", "🇹🇷 Türkçe")
TR  = dil == "🇹🇷 Türkçe"
DB  = st.session_state.get("db_aktif", False)

st.title("🔬 " + ("Hasta Bitki Teşhis" if TR else "Plant Diagnosis"))
st.caption("Belirtileri girerek bitkinin sorununu öğrenin." if TR else "Enter symptoms to diagnose your plant.")
st.divider()

plants = st.session_state.get("plants", [])

if not plants:
    st.info("Önce Bitki Kütüphanesi'nden bitki ekleyin." if TR else "Add plants from the Library first.")
    st.stop()

# Sağlık etkisi tablosu — her belirti kaç puan düşürür
SAGLIK_ETKISI = {
    # yaprak_durumu → puan
    "Normal":             0,
    "Sararma":           -20,
    "Kahverengi Uçlar":  -10,
    "Kahverengi Lekeler":-15,
    "Beyaz Lekeler":     -15,
    "Delikler":          -25,
    "Düşen Yapraklar":   -15,
    "Solma":             -10,
    # toprak_nemi ek etkisi
    "Kuru_ek":           -10,
    "Islak_ek":          -15,
    # ışık ek etkisi
    "Çok Az_ek":          -5,
    "Çok Fazla_ek":       -5,
    # sıcaklık ek etkisi
    "Soğuk (<15°C)_ek":   -5,
    "Sıcak (>30°C)_ek":   -5,
}

with st.container(border=True):
    secilen = st.selectbox(
        "🌿 " + ("Hangi bitkiniz hasta?" if TR else "Which plant is sick?"),
        [p["ad"] for p in plants]
    )
    bitki = next(p for p in plants if p["ad"] == secilen)

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        yaprak_secenekler = ["Normal","Sararma","Kahverengi Uçlar","Kahverengi Lekeler","Beyaz Lekeler","Delikler","Düşen Yapraklar","Solma"]
        yaprak_en = ["Normal","Yellowing","Brown Tips","Brown Spots","White Spots","Holes","Dropping Leaves","Wilting"]
        yaprak_idx = st.selectbox(
            "🍃 " + ("Yaprak Durumu" if TR else "Leaf Condition"),
            range(len(yaprak_secenekler)),
            format_func=lambda i: yaprak_secenekler[i] if TR else yaprak_en[i]
        )
        yaprak = yaprak_secenekler[yaprak_idx]

    with col2:
        toprak_sec = ["Normal","Kuru","Islak"]
        toprak_en  = ["Normal","Dry","Wet"]
        toprak_idx = st.selectbox(
            "💧 " + ("Toprak Nemi" if TR else "Soil Moisture"),
            range(len(toprak_sec)),
            format_func=lambda i: toprak_sec[i] if TR else toprak_en[i]
        )
        toprak = toprak_sec[toprak_idx]

    col3, col4 = st.columns(2)
    with col3:
        isik_sec = ["Yeterli","Çok Az","Çok Fazla"]
        isik_en  = ["Sufficient","Too Little","Too Much"]
        isik_idx = st.selectbox(
            "☀️ " + ("Işık Durumu" if TR else "Light Condition"),
            range(len(isik_sec)),
            format_func=lambda i: isik_sec[i] if TR else isik_en[i]
        )
        isik = isik_sec[isik_idx]

    with col4:
        sicak_sec = ["Normal (18-25°C)","Soğuk (<15°C)","Sıcak (>30°C)"]
        sicak_en  = ["Normal (18-25°C)","Cold (<15°C)","Hot (>30°C)"]
        sicak_idx = st.selectbox(
            "🌡️ " + ("Sıcaklık" if TR else "Temperature"),
            range(len(sicak_sec)),
            format_func=lambda i: sicak_sec[i] if TR else sicak_en[i]
        )
        sicaklik = sicak_sec[sicak_idx]

    st.divider()

    if st.button("🔍 " + ("Teşhis Yap" if TR else "Diagnose"), use_container_width=True, type="primary"):
        sonuc = hastalik_tespit(yaprak, toprak)

        # Ek sorunlar listesi
        ek_sorunlar = []
        if isik == "Çok Az":
            ek_sorunlar.append(("Yetersiz ışık" if TR else "Insufficient light", "orta",
                                 "Bitkiyi daha aydınlık bir yere taşı." if TR else "Move to a brighter spot."))
        elif isik == "Çok Fazla":
            ek_sorunlar.append(("Aşırı güneş" if TR else "Too much sun", "orta",
                                 "Direkt güneşten koru." if TR else "Protect from direct sunlight."))
        if sicaklik == "Soğuk (<15°C)":
            ek_sorunlar.append(("Soğuk stresi" if TR else "Cold stress", "orta",
                                 "Bitkiyi sıcak bir yere taşı." if TR else "Move to a warmer spot."))
        elif sicaklik == "Sıcak (>30°C)":
            ek_sorunlar.append(("Sıcaklık stresi" if TR else "Heat stress", "orta",
                                 "Serin bir yere taşı, daha sık sula." if TR else "Move to a cooler spot, water more."))

        # ── SAĞLIK PUANI HESAPLA ──
        puan_degisimi = SAGLIK_ETKISI.get(yaprak, 0)
        if toprak != "Normal":
            puan_degisimi += SAGLIK_ETKISI.get(f"{toprak}_ek", 0)
        if isik != "Yeterli":
            puan_degisimi += SAGLIK_ETKISI.get(f"{isik}_ek", 0)
        if sicaklik != "Normal (18-25°C)":
            puan_degisimi += SAGLIK_ETKISI.get(f"{sicaklik}_ek", 0)

        eski_saglik = bitki["saglik"]
        yeni_saglik = max(5, min(100, eski_saglik + puan_degisimi))

        # Session'u güncelle
        for bp in st.session_state.plants:
            if bp["id"] == bitki["id"]:
                bp["saglik"] = yeni_saglik
                break

        # DB'ye kaydet
        if DB and puan_degisimi != 0:
            try:
                from database_handler import bitki_guncelle
                bitki_guncelle(bitki["id"], yeni_saglik=yeni_saglik)
            except Exception as e:
                print("Sağlık güncelleme hatası:", e)

        # ── SONUÇ GÖSTER ──
        st.divider()
        st.subheader("📋 " + ("Teşhis Sonucu" if TR else "Diagnosis Result"))

        ikon = {"yok": "✅", "orta": "⚠️", "yuksek": "🚨"}.get(sonuc["tehlike_seviyesi"], "ℹ️")

        if sonuc["tehlike_seviyesi"] == "yok":
            st.success(f"{ikon} **{sonuc['teshis']}**\n\n💡 {sonuc['oneri']}")
        elif sonuc["tehlike_seviyesi"] == "orta":
            st.warning(f"{ikon} **{sonuc['teshis']}**\n\n💡 {sonuc['oneri']}")
        else:
            st.error(f"{ikon} **{sonuc['teshis']}**\n\n💡 {sonuc['oneri']}")

        for sorun, seviye, oneri in ek_sorunlar:
            st.warning(f"⚠️ **{sorun}**\n\n💡 {oneri}")

        # ── SAĞLIK DEĞİŞİMİ GÖSTER ──
        st.divider()
        if puan_degisimi < 0:
            st.error(f"📉 **{'Sağlık güncellemesi' if TR else 'Health update'}:** {eski_saglik}% → {yeni_saglik}% ({puan_degisimi})")
        elif puan_degisimi == 0:
            st.success(f"💚 **{'Sağlık değişmedi' if TR else 'Health unchanged'}:** %{yeni_saglik}")
        else:
            st.success(f"📈 **{'Sağlık iyileşti' if TR else 'Health improved'}:** {eski_saglik}% → {yeni_saglik}% (+{puan_degisimi})")

        st.progress(yeni_saglik / 100)

        # ── BİTKİ BAKIM HATIRLATICI ──
        st.divider()
        st.subheader(f"📌 {bitki['ad']} — " + ("Bakım Özeti" if TR else "Care Summary"))
        c1, c2, c3 = st.columns(3)
        c1.metric("Sulama" if TR else "Watering", f"{'Her' if TR else 'Every'} {bitki['sulama_periyodu']} {'günde bir' if TR else 'days'}")
        isik_sozluk = {"Indirect sunlight": "Dolaylı Güneş", "Part shade": "Yarı Gölge", "Full sun": "Tam Güneş", "Bright indirect": "Parlak Dolaylı", "Unknown": "Bilinmiyor"}
        gosterilen_isik = isik_sozluk.get(bitki["isik"], bitki["isik"]) if TR else bitki["isik"]
        c2.metric("Işık" if TR else "Light", gosterilen_isik)
        loc_map = {"Salon": "Living Room", "Mutfak": "Kitchen", "Yatak Odası": "Bedroom", "Ofis": "Office", "Balkon": "Balcony", "Banyo": "Bathroom", "Bahçe": "Garden"}
        en_to_tr = {v: k for k, v in loc_map.items()}
        gosterilen_konum = en_to_tr.get(bitki["konum"], bitki["konum"]) if TR else loc_map.get(bitki["konum"], bitki["konum"])
        
        c3.metric("Konum" if TR else "Location", gosterilen_konum)