import streamlit as st
import datetime
from weather_service import hava_durumu_kontrol

if not st.session_state.get("logged_in"):
    st.warning("Lütfen önce giriş yapın.")
    st.stop()

plants = st.session_state.get("plants", [])

# ─────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────
st.title("🌿 Panel")
st.caption(f"{len(plants)} Sağlıklı Bitki")
st.divider()

# ── Gerçek hava durumu (OpenWeatherMap) ──
hava = hava_durumu_kontrol("Elazig")  # weather_service.py → hava_durumu_kontrol(sehir)

col_hava, col_bilgi = st.columns([1, 3])
with col_hava:
    if hava:
        st.metric("🌡️ Sıcaklık", f"{hava['sicaklik']:.1f}°C", hava["durum"])
    else:
        st.metric("🌡️ Sıcaklık", "—", "Bağlantı yok")
with col_bilgi:
    if hava and hava["yagmur_var_mi"]:
        st.warning("🌧️ **Bugün yağmur var.** Dış mekân bitkilerini sulamayın.")
    elif hava:
        st.info(f"☀️ **Hava:** {hava['durum']} — {hava['sicaklik']:.1f}°C. Yağış beklenmez.")
    else:
        st.info("Hava durumu verisi alınamadı.")

st.divider()

# ── Üst metrikler ──
avg_saglik = int(sum(p["saglik"] for p in plants) / len(plants)) if plants else 0
thirsty    = [p for p in plants if p["sulama_periyodu"] <= 3]

m1, m2, m3 = st.columns(3)
m1.metric("SAĞLIK SKORU",   f"%{avg_saglik}", "+1%")
m2.metric("BİTKİLER",       str(len(plants)), "Aktif")
m3.metric("BEKLEYEN GÖREV", str(len(thirsty)),"Bugün")

st.divider()

# ── Sol: Susayanlar | Sağ: Bitki detayı ──
sol, sag = st.columns([1, 1.6])

with sol:
    st.subheader("💧 Bugün Susayanlar")
    # Yağmur varsa dış bitkiler listeden çıkar
    filtreli_thirsty = thirsty
    if hava and hava["yagmur_var_mi"]:
        filtreli_thirsty = [p for p in thirsty if p["konum"] not in ["Balkon", "Bahçe"]]
        if len(filtreli_thirsty) < len(thirsty):
            st.caption("🌧️ Dış mekân bitkiler yağmur nedeniyle listeden çıkarıldı.")

    if filtreli_thirsty:
        for p in filtreli_thirsty:
            st.checkbox(f"**{p['ad']}** — sulama gerekli", key=f"c_{p['ad']}")
    else:
        st.success("Bugün sulama gerekenler yok 🎉")

    st.divider()
    st.info("🌱 **Haftalık İpucu:** Bitkilerinizi sabah saatlerinde sulamak mantar oluşumunu engeller.")

with sag:
    if plants:
        secilen = st.selectbox("Bitki seçin", [p["ad"] for p in plants])
        p = next(x for x in plants if x["ad"] == secilen)

        st.subheader(f"🪴 {p['ad']}")
        st.caption(f"*{p['tur']}*")

        c1, c2, c3 = st.columns(3)
        c1.metric("Konum",   p["konum"])
        c2.metric("Sulama",  f"{p['sulama_periyodu']} günde bir")
        c3.metric("Işık",    p["isik"])

        st.write("**Sağlık Durumu**")
        st.progress(p["saglik"] / 100)
        label = "Çok Sağlıklı 💚" if p["saglik"] >= 80 else "Orta 🟡" if p["saglik"] >= 50 else "Hasta 🔴"
        st.caption(f"%{p['saglik']} — {label}")

        b1, b2 = st.columns(2)
        with b1:
            if st.button("✅ Sulandı", use_container_width=True):
                st.success(f"{p['ad']} sulandı!")
        with b2:
            if st.button("📝 Not Ekle", use_container_width=True):
                st.info("Not özelliği Kütüphane sayfasında.")

st.divider()
st.subheader("🕐 Yaklaşan Görevler")
g1, g2 = st.columns(2)
with g1:
    st.write("🍃 Yaprak Temizliği")
    st.caption("Yarın")
with g2:
    st.write("🪴 Saksı Değişimi")
    st.caption("2 ay sonra")
