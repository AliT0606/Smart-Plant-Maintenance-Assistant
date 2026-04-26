import streamlit as st
import datetime

if not st.session_state.get("logged_in"):
    st.warning("Lütfen önce giriş yapın.")
    st.stop()

plants = st.session_state.get("plants", [])

# ─────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────
st.title("🌿 Dashboard")
st.caption(f"{len(plants)} Sağlıklı Bitki")
st.divider()

# ── Mock hava durumu ──
col_hava, col_bilgi = st.columns([1, 3])
with col_hava:
    st.metric("☀️ Sıcaklık", "24°C", "Elazığ, TR")
with col_bilgi:
    st.info("**Akıllı Tahmin:** Bugün UV yüksek. Hassas bitkilerinizi doğrudan güneşten uzak tutun. Yağış beklenmez.")

st.divider()

# ── Üst metrikler ──
avg_saglik = int(sum(p["saglik"] for p in plants) / len(plants)) if plants else 0
thirsty    = [p for p in plants if p["sulama_periyodu"] <= 3]

m1, m2, m3 = st.columns(3)
m1.metric("SAĞLIK SKORU",  f"%{avg_saglik}", "+1%")
m2.metric("BİTKİLER",      str(len(plants)), "Aktif")
m3.metric("BEKLEYEN GÖREV", str(len(thirsty)), "Bugün")

st.divider()

# ── Sol: Susayanlar | Sağ: Bitki detayı ──
sol, sag = st.columns([1, 1.6])

with sol:
    st.subheader("💧 Bugün Susayanlar")
    if thirsty:
        for p in thirsty:
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
        c1.metric("Konum",      p["konum"])
        c2.metric("Sulama",     f"{p['sulama_periyodu']} günde bir")
        c3.metric("Işık",       p["isik"])

        st.write("")
        st.write("**Sağlık Durumu**")
        st.progress(p["saglik"] / 100)
        label = "Çok Sağlıklı 💚" if p["saglik"] >= 80 else "Orta 🟡" if p["saglik"] >= 50 else "Hasta 🔴"
        st.caption(f"%{p['saglik']} — {label}")

        b1, b2 = st.columns(2)
        with b1:
            if st.button("✅ Sulandı", use_container_width=True, key="sulandi"):
                st.success(f"{p['ad']} sulandı olarak işaretlendi!")
        with b2:
            if st.button("📝 Not Ekle", use_container_width=True, key="not"):
                st.info("Not özelliği Kütüphane sayfasında.")

st.divider()

# ── Alt: Yaklaşan görevler ──
st.subheader("🕐 Yaklaşan Görevler")
g1, g2 = st.columns(2)
with g1:
    st.write("🍃 Yaprak Temizliği")
    st.caption("Yarın")
with g2:
    st.write("🪴 Saksı Değişimi")
    st.caption("2 ay sonra")
