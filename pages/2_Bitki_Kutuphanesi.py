import streamlit as st
import datetime
from database_handler import akilli_bitki_ekle, tum_bitkileri_getir, bitki_sil
from perenual_service import bitki_bilgisi_getir

if not st.session_state.get("logged_in"):
    st.warning("Lütfen önce giriş yapın.")
    st.stop()

# ─────────────────────────────────────────
# BİTKİ KÜTÜPHANESİ
# ─────────────────────────────────────────
st.title("📚 Bitki Kütüphanesi")
st.caption(f"Koleksiyonunuzda {len(st.session_state.plants)} bitki var.")
st.divider()

tab_liste, tab_ekle, tab_notlar = st.tabs(["🌿 Koleksiyonum", "➕ Yeni Bitki Ekle", "📝 Notlar"])

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

                    
                    if st.button("🗑️ Sil", key=f"sil_db_{p['id']}", use_container_width=True):
                        # 1. Veritabanından sil
                        try:
                            bitki_sil(p["id"])
                        except Exception:
                            pass
                        # 2. Arayüzden anında kaldır
                        st.session_state.plants = [b for b in st.session_state.plants if b["id"] != p["id"]]
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
                    # 1. API'den veriyi anlık olarak çekiyoruz
                    api_bilgileri = bitki_bilgisi_getir(yeni_tur)
                    
                    # Varsayılan değerler
                    sulama_gun = 7
                    isik_bilgisi = "Bilinmiyor"
                    
                    # API cevap verdiyse gerçek değerleri al
                    if api_bilgileri:
                        sulama_gun = api_bilgileri.get("periyot_gun", 7)
                        isik_bilgisi = api_bilgileri.get("isik", "Bilinmiyor")

                    try:
                        # 2. DB'ye ekleme işlemi
                        akilli_bitki_ekle(
                            ad=yeni_ad,
                            tur=yeni_tur,
                            ekim_tarihi=str(yeni_tarih),
                            konum=yeni_konum
                        )
                        # DB başarılıysa verileri çek
                        rows = tum_bitkileri_getir()
                        if rows:
                            guncel_bitkiler = []
                            for row in rows:
                                bitki_id = row[0]
                                ad = row[1]
                                
                                # DB'de isik sütunu olmadığı için, az önce eklediğimiz bitkiyse API verisini kullan, eskiyse Bilinmiyor yap
                                guncel_isik = isik_bilgisi if ad == yeni_ad else "Bilinmiyor"
                                guncel_sulama = sulama_gun if ad == yeni_ad else row[4]
                                
                                guncel_bitkiler.append({
                                    "id":             bitki_id,
                                    "ad":             ad,
                                    "tur":            row[2],
                                    "ekim_tarihi":    row[3],
                                    "sulama_periyodu":guncel_sulama,
                                    "konum":          row[5],
                                    "saglik":         80,
                                    "isik":           guncel_isik,
                                })
                            st.session_state.plants = guncel_bitkiler

                    except Exception:
                        # DB çalışmıyorsa doğrudan session_state'e ekle (Mock Modu)
                        yeni_id = max((p["id"] for p in st.session_state.plants), default=0) + 1
                        st.session_state.plants.append({
                            "id":             yeni_id,
                            "ad":             yeni_ad,
                            "tur":            yeni_tur,
                            "ekim_tarihi":    str(yeni_tarih),
                            "sulama_periyodu": sulama_gun,
                            "konum":          yeni_konum,
                            "saglik":         80,
                            "isik":           isik_bilgisi,
                        })
                        
                st.success(f"✅ **{yeni_ad}** koleksiyona eklendi!")
                st.rerun()
            else:
                st.error("Lütfen bitki adı ve türünü girin.")

# ── TAB 3: Notlar ──
with tab_notlar:
    st.subheader("📝 Bitki Notları")

    if not st.session_state.plants:
        st.info("Önce bir bitki ekleyin.")
    else:
        secilen_bitki = st.selectbox(
            "Bitki seçin",
            [p["ad"] for p in st.session_state.plants],
            key="not_bitki_sec"
        )
        secilen_p = next(p for p in st.session_state.plants if p["ad"] == secilen_bitki)

        # Notları session_state'te tut (dict: bitki_id -> [notlar])
        if "notlar" not in st.session_state:
            st.session_state.notlar = {}

        bitki_notlar = st.session_state.notlar.get(secilen_p["id"], [])

        # Mevcut notları göster
        if bitki_notlar:
            for n in reversed(bitki_notlar):
                with st.container(border=True):
                    st.caption(n["tarih"])
                    st.write(n["icerik"])
        else:
            st.info("Bu bitki için henüz not yok.")

        st.divider()

        # Yeni not ekle
        yeni_not = st.text_area("Yeni not", placeholder="Yapraklarda sararma görüldü...")
        if st.button("💾 Notu Kaydet", use_container_width=True):
            if yeni_not.strip():
                if secilen_p["id"] not in st.session_state.notlar:
                    st.session_state.notlar[secilen_p["id"]] = []
                st.session_state.notlar[secilen_p["id"]].append({
                    "icerik": yeni_not.strip(),
                    "tarih":  str(datetime.date.today())
                })
                st.success("Not kaydedildi!")
                st.rerun()
            else:
                st.error("Not boş olamaz.")
