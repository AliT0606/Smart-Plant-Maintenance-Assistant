import streamlit as st
import datetime

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
    ara = st.text_input("🔍 Bitki Ara", placeholder="İsim veya tür yazın...")
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
                    c1.metric("Konum",   p["konum"])
                    c2.metric("Sulama",  f"{p['sulama_periyodu']}g/bir")
                    c3.metric("Sağlık",  f"%{p['saglik']}")
                    st.write(f"☀️ {p['isik']}  —  {saglik_label}")

                    d1, d2 = st.columns(2)
                    with d1:
                        if st.button("🗑️ Sil", key=f"sil_{i}", use_container_width=True):
                            st.session_state.plants.pop(i)
                            st.rerun()
                    with d2:
                        if st.button("✏️ Düzenle", key=f"duzenle_{i}", use_container_width=True):
                            st.session_state[f"edit_{i}"] = not st.session_state.get(f"edit_{i}", False)

                if st.session_state.get(f"edit_{i}"):
                    with st.expander("Düzenleme", expanded=True):
                        yeni_ad  = st.text_input("Ad",    value=p["ad"],    key=f"ead_{i}")
                        yeni_kon = st.selectbox("Konum", ["Salon","Mutfak","Yatak Odası","Ofis","Balkon","Banyo"], key=f"ekon_{i}")
                        yeni_sag = st.slider("Sağlık %", 0, 100, p["saglik"], key=f"esag_{i}")
                        if st.button("Kaydet", key=f"kaydet_{i}"):
                            st.session_state.plants[i]["ad"]     = yeni_ad
                            st.session_state.plants[i]["konum"]  = yeni_kon
                            st.session_state.plants[i]["saglik"] = yeni_sag
                            st.session_state[f"edit_{i}"]        = False
                            st.rerun()

# ── TAB 2: Ekle ──
with tab_ekle:
    st.subheader("🌱 Yeni Bitki Ekle")
    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            yeni_ad      = st.text_input("Bitki Adı",       placeholder="Barış Çiçeği")
            yeni_tur     = st.text_input("Tür (Latince)",   placeholder="Spathiphyllum")
            yeni_konum   = st.selectbox("Konum", ["Salon","Mutfak","Yatak Odası","Ofis","Balkon","Banyo"])
        with c2:
            yeni_isik    = st.selectbox("Işık İhtiyacı",    ["Tam Güneş","Dolaylı Güneş","Parlak Dolaylı","Az Işık"])
            yeni_periyot = st.number_input("Sulama Periyodu (gün)", min_value=1, max_value=30, value=7)
            yeni_saglik  = st.slider("Başlangıç Sağlığı %", 0, 100, 80)

        if st.button("🌿 Koleksiyona Ekle", use_container_width=True):
            if yeni_ad and yeni_tur:
                st.session_state.plants.append({
                    "ad":             yeni_ad,
                    "tur":            yeni_tur,
                    "konum":          yeni_konum,
                    "sulama_periyodu":yeni_periyot,
                    "saglik":         yeni_saglik,
                    "isik":           yeni_isik,
                })
                st.success(f"✅ {yeni_ad} koleksiyona eklendi!")
                st.rerun()
            else:
                st.error("Lütfen bitki adı ve türünü girin.")
