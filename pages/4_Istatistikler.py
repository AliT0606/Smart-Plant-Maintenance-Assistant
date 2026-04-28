import streamlit as st
import pandas as pd
import datetime
import random
from collections import Counter
from database_handler import tum_bitkileri_getir

if not st.session_state.get("logged_in"):
    st.warning("Lütfen önce giriş yapın.")
    st.stop()

# ─────────────────────────────────────────
# İSTATİSTİKLER
# ─────────────────────────────────────────
st.title("📊 İstatistikler")
st.caption("Bahçenizin genel sağlık ve bakım analizi.")
st.divider()

# DB'den güncel listeyi çek
if st.button("🔄 Veritabanından Yenile"):
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
    st.rerun()

plants = st.session_state.get("plants", [])

if not plants:
    st.info("İstatistik görmek için önce Bitki Kütüphanesi'nden bitki ekleyin.")
    st.stop()

avg_saglik = int(sum(p["saglik"] for p in plants) / len(plants))
en_iyi     = max(plants, key=lambda p: p["saglik"])
en_kotu    = min(plants, key=lambda p: p["saglik"])

# ── Üst metrikler ──
m1, m2, m3, m4 = st.columns(4)
m1.metric("Ort. Sağlık",    f"%{avg_saglik}")
m2.metric("En Sağlıklı",    en_iyi["ad"],  f"%{en_iyi['saglik']}")
m3.metric("Dikkat Gereken", en_kotu["ad"], f"%{en_kotu['saglik']}")
m4.metric("Toplam Bitki",   len(plants))

st.divider()

# ── Sağlık çubukları ──
st.subheader("🌡️ Bitki Sağlık Durumları")
for p in sorted(plants, key=lambda x: x["saglik"], reverse=True):
    c1, c2 = st.columns([1, 4])
    with c1:
        st.write(p["ad"])
    with c2:
        st.progress(p["saglik"] / 100)
        st.caption(f"%{p['saglik']}")

st.divider()

# ── Dağılım grafikleri ──
col_sol, col_sag = st.columns(2)

with col_sol:
    st.subheader("🏠 Konuma Göre Dağılım")
    konum_sayac = Counter(p["konum"] for p in plants)
    df_konum    = pd.DataFrame(konum_sayac.items(), columns=["Konum", "Bitki Sayısı"])
    st.bar_chart(df_konum.set_index("Konum"))

with col_sag:
    st.subheader("💧 Sulama Periyodu Dağılımı (DB)")
    # sulama_periyodu DB'den gelen gerçek değer
    periyot_sayac = Counter(
        "Az (>7g)"   if p["sulama_periyodu"] > 7 else
        "Orta (4-7g)"if p["sulama_periyodu"] >= 4 else
        "Sık (<4g)"
        for p in plants
    )
    df_periyot = pd.DataFrame(periyot_sayac.items(), columns=["Sulama", "Bitki Sayısı"])
    st.bar_chart(df_periyot.set_index("Sulama"))

st.divider()

# ── 30 Günlük trend (simüle — DB'de tarihsel veri olmadığı için) ──
st.subheader("📈 Son 30 Gün Sağlık Trendi")
random.seed(42)
tarihler    = [datetime.date.today() - datetime.timedelta(days=i) for i in range(29, -1, -1)]
saglik_data = [max(0, min(100, avg_saglik + random.randint(-8, 8))) for _ in tarihler]
df_trend    = pd.DataFrame({"Tarih": tarihler, "Ortalama Sağlık (%)": saglik_data})
st.line_chart(df_trend.set_index("Tarih"))

st.divider()

# ── Bakım puanı ──
skor  = min(100, avg_saglik + len(plants) * 2)
label = "Mükemmel Bahçıvan 🏆" if skor >= 90 else "İyi Bahçıvan 🌿" if skor >= 70 else "Gelişiyor 🌱"
st.subheader(f"🎯 Bakım Puanınız: {skor}/100 — {label}")
st.progress(skor / 100)
