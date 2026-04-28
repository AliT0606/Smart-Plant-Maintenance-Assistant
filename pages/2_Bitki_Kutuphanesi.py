import streamlit as st
import datetime
from database_handler import akilli_bitki_ekle, tum_bitkileri_getir

if not st.session_state.get("logged_in"):
    st.warning("Lütfen önce giriş yapın.")
    st.stop()

# ─────────────────────────────────────────
# BİTKİ KÜTÜPHANESİ
# ─────────────────────────────────────────
st.title("📚 Bitki Kütüphanesi")
st.caption(f"Koleksiyonunuzda {len(st.session_state.plants)} bitki var.")
st.divider()

tab_liste, tab_ekle = st.tabs(["🌿 Koleksiyonum", "➕ Yeni Bitki Ekle"])

# ── TAB 1: Liste ──
with tab_liste:
    ara    = st.text_input("🔍 Bitki Ara", placeholder="İsim veya tür yazın...")
    plants = st.session_state.plants
    if ara:
        plants = [p for p in plants if ara.lower() in p["ad"].lower() or ara.lower() in p["tur"].lower()]

    if not plants:
        st.info("Sonuç bulunamadı.")
    else:
        sol, sag = st.columns(2)
        for i, p in enumerate(plants):
            with (sol if i % 2 == 0 else sag):
                saglik_label = "💚 Çok Sağlıklı" if p["saglik"] >= 80 else "🟡 Orta" if p["saglik"] >= 50 else "🔴 Hasta"
                with st.container(border=True):
                    st.subheader(p["ad"])
                    st.caption(f"*{p['tur']}*")
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Konum",  p["konum"])
                    c2.metric("Sulama", f"{p['sulama_periyodu']}g/bir")
                    c3.metric("Sağlık", f"%{p['saglik']}")
                    st.write(f"☀️ {p['isik']}  —  {saglik_label}")

                    # NOT: Silme işlemi için database_handler'a sil fonksiyonu eklenirse buraya gelecek
                    # Şimdilik sadece session_state'ten siliyoruz
                    if st.button("🗑️ Sil", key=f"sil_{i}", use_container_width=True):
                        st.session_state.plants.pop(i)
                        st.rerun()

# ── TAB 2: Ekle ──
with tab_ekle:
    st.subheader("🌱 Yeni Bitki Ekle")
    st.caption("Bitki türü girilince Perenual API'den sulama ve ışık bilgisi otomatik gelir.")

    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            yeni_ad    = st.text_input("Bitki Adı",     placeholder="Barış Çiçeği")
            yeni_tur   = st.text_input("Tür (Latince)", placeholder="Spathiphyllum")
            yeni_konum = st.selectbox("Konum", ["Salon","Mutfak","Yatak Odası","Ofis","Balkon","Banyo"])
        with c2:
            yeni_tarih = st.date_input("Ekim Tarihi", datetime.date.today())

        if st.button("🌿 Koleksiyona Ekle", use_container_width=True):
            if yeni_ad and yeni_tur:
                with st.spinner("Perenual API'den bitki bilgisi alınıyor..."):
                    # akilli_bitki_ekle → database_handler.py
                    # İçinde bitki_bilgisi_getir(tur) çağırıp DB'ye yazar
                    akilli_bitki_ekle(
                        ad=yeni_ad,
                        tur=yeni_tur,
                        ekim_tarihi=str(yeni_tarih),
                        konum=yeni_konum
                    )

                # DB'den güncel listeyi çek ve session'a yükle
                rows = tum_bitkileri_getir()
                if rows:
                    st.session_state.plants = [
                        {
                            "id":             row[0],
                            "ad":             row[1],
                            "tur":            row[2],
                            "ekim_tarihi":    row[3],
                            "sulama_periyodu":row[4],
                            "konum":          row[5],
                            "saglik":         80,
                            "isik":           "Bilinmiyor",
                        }
                        for row in rows
                    ]
                st.success(f"✅ **{yeni_ad}** Perenual API üzerinden bilgileri alınarak veritabanına eklendi!")
                st.rerun()
            else:
                st.error("Lütfen bitki adı ve türünü girin.")
