import streamlit as st
import pandas as pd
import datetime
import random
from collections import Counter

if not st.session_state.get("logged_in"):
    st.switch_page("app.py")

dil    = st.session_state.get("dil", "🇹🇷 Türkçe")
TR     = dil == "🇹🇷 Türkçe"
DB     = st.session_state.get("db_aktif", False)

st.title("📊 " + ("İstatistikler" if TR else "Statistics"))
st.caption("Bahçenizin genel sağlık ve bakım analizi." if TR else "Overall health and care analysis of your garden.")
st.divider()

if DB:
    if st.button("🔄 Veritabanından Yenile"):
        try:
            from database_handler import tum_bitkileri_getir
            from perenual_service import bitki_bilgisi_getir
            rows = tum_bitkileri_getir()
            if rows:
                st.session_state.plants = [
                    {"id": r[0], "ad": r[1], "tur": r[2], "ekim_tarihi": r[3],
                     "sulama_periyodu": r[4], "konum": r[5],
                     "saglik": r[6] if r[6] else 80,  # ✅ DB'deki değeri kullan
                     "isik": (bitki_bilgisi_getir(r[2]) or {}).get("isik", "Bilinmiyor"),
                     "son_sulama": str(r[7]) if r[7] else None}
                    for r in rows
                ]
            st.rerun()
        except Exception as e:
            st.error(f"DB hatası: {e}")

plants = st.session_state.get("plants", [])

if not plants:
    st.info("İstatistik görmek için önce bitki ekleyin." if TR else "Add plants to see statistics.")
    st.stop()

avg_saglik = int(sum(p["saglik"] for p in plants) / len(plants))
en_iyi     = max(plants, key=lambda p: p["saglik"])
en_kotu    = min(plants, key=lambda p: p["saglik"])

m1, m2, m3, m4 = st.columns(4)
m1.metric("Ort. Sağlık" if TR else "Avg. Health",      f"%{avg_saglik}")
m2.metric("En Sağlıklı" if TR else "Healthiest",        en_iyi["ad"],  f"%{en_iyi['saglik']}")
m3.metric("Dikkat Gereken" if TR else "Needs Attention", en_kotu["ad"], f"%{en_kotu['saglik']}")
m4.metric("Toplam Bitki" if TR else "Total Plants",      len(plants))

st.divider()

st.subheader("🌡️ " + ("Bitki Sağlık Durumları" if TR else "Plant Health Status"))
for p in sorted(plants, key=lambda x: x["saglik"], reverse=True):
    c1, c2 = st.columns([1, 4])
    with c1:
        st.write(p["ad"])
    with c2:
        st.progress(p["saglik"] / 100)
        st.caption(f"%{p['saglik']}")

st.divider()

col_sol, col_sag = st.columns(2)

with col_sol:
    st.subheader("🏠 " + ("Konuma Göre Dağılım" if TR else "Distribution by Location"))
    konum_sayac = Counter(p["konum"] for p in plants)
    df_konum    = pd.DataFrame(konum_sayac.items(), columns=["Konum" if TR else "Location", "Bitki Sayısı" if TR else "Count"])
    st.bar_chart(df_konum.set_index("Konum" if TR else "Location"))

with col_sag:
    st.subheader("💧 " + ("Sulama Periyodu Dağılımı" if TR else "Watering Frequency"))
    periyot_sayac = Counter(
        ("Az (>7g)" if TR else "Low (>7d)")    if p["sulama_periyodu"] > 7  else
        ("Orta (4-7g)" if TR else "Med (4-7d)") if p["sulama_periyodu"] >= 4 else
        ("Sık (<4g)" if TR else "High (<4d)")
        for p in plants
    )
    df_periyot = pd.DataFrame(periyot_sayac.items(), columns=["Sulama" if TR else "Watering", "Bitki Sayısı" if TR else "Count"])
    st.bar_chart(df_periyot.set_index("Sulama" if TR else "Watering"))

st.divider()

# Sulama gecikme analizi
bugun = datetime.date.today()
st.subheader("⏰ " + ("Sulama Gecikme Analizi" if TR else "Watering Delay Analysis"))
gecikme_data = []
for p in plants:
    son = p.get("son_sulama")
    if son:
        try:
            sonraki = datetime.date.fromisoformat(str(son)[:10]) + datetime.timedelta(days=p["sulama_periyodu"])
            gecikme = max(0, (bugun - sonraki).days)
        except Exception:
            gecikme = 0
    else:
        gecikme = p["sulama_periyodu"]
    gecikme_data.append({"Bitki" if TR else "Plant": p["ad"], "Gecikme (Gün)" if TR else "Delay (Days)": gecikme})

df_gecikme = pd.DataFrame(gecikme_data)
st.bar_chart(df_gecikme.set_index("Bitki" if TR else "Plant"))

st.divider()

st.subheader("📈 " + ("Son 30 Gün Sağlık Trendi" if TR else "Last 30 Days Health Trend"))
random.seed(42)
tarihler    = [datetime.date.today() - datetime.timedelta(days=i) for i in range(29, -1, -1)]
saglik_data = [max(0, min(100, avg_saglik + random.randint(-8, 8))) for _ in tarihler]
col_label   = "Ortalama Sağlık (%)" if TR else "Average Health (%)"
df_trend    = pd.DataFrame({"Tarih": tarihler, col_label: saglik_data})
st.line_chart(df_trend.set_index("Tarih"))

st.divider()

# 1. Hasta bitki sayısını bul (Sağlığı 60'ın altında olanlar)
hasta_bitki_sayisi = sum(1 for p in plants if p["saglik"] < 60)

# 2. Yeni Algoritma: Ortalama - (Hasta Bitki Başına 15 Ceza Puanı) + (Sadece bitki adedi kadar minik bonus)
skor = int(max(0, min(100, avg_saglik - (hasta_bitki_sayisi * 15) + len(plants))))

if skor >= 90:
    label = "Mükemmel Bahçıvan 🏆" if TR else "Expert Gardener 🏆"
elif skor >= 70:
    label = "İyi Bahçıvan 🌿" if TR else "Good Gardener 🌿"
elif skor >= 40:
    label = "Gelişiyor 🌱" if TR else "Improving 🌱"
else:
    label = "Bahçıvanlık Zor İş 🥀" if TR else "Needs Much Improvement 🥀"

st.subheader(f"🎯 {'Bakım Puanınız' if TR else 'Care Score'}: {skor}/100 — {label}")
st.progress(skor / 100)