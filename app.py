import streamlit as st

# ─────────────────────────────────────────
# SAYFA AYARLARI
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Killi Bahçe",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────
# GLOBAL TEMA
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background-color: #f5f0e8 !important;
    color: #2a2e27 !important;
}
section[data-testid="stSidebar"] {
    background-color: #ede8dd !important;
}
.stButton > button {
    background: linear-gradient(135deg, #1a3a1a, #2d5a27) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 50px !important;
    font-weight: 600 !important;
}
.stTextInput > div > div > input {
    background-color: #edeade !important;
    border-radius: 12px !important;
    border: 1.5px solid #ccc8bc !important;
}
[data-testid="metric-container"] {
    background: #edeade;
    border-radius: 16px;
    padding: 14px 18px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 50px !important;
    font-weight: 500 !important;
}
.stTabs [aria-selected="true"] {
    background: #1a3a1a !important;
    color: #fff !important;
}
.stProgress > div > div > div {
    background: #2d5a27 !important;
    border-radius: 99px;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# BACKEND İMPORT
# ─────────────────────────────────────────
from database_handler import tum_bitkileri_getir

# ─────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# DB'den bitkileri yükle (uygulama ilk açıldığında bir kez)
if "plants" not in st.session_state:
    rows = tum_bitkileri_getir()
    if rows:
        # tum_bitkileri_getir() → SELECT * FROM Bitkiler
        # Sütun sırası: Id, Ad, Tur, EkimTarihi, SulamaPeriyodu, Konum
        st.session_state.plants = [
            {
                "id":             row[0],
                "ad":             row[1],
                "tur":            row[2],
                "ekim_tarihi":    row[3],
                "sulama_periyodu":row[4],
                "konum":          row[5],
                "saglik":         80,    # DB'de sağlık sütunu yoksa varsayılan
                "isik":           "Bilinmiyor",
            }
            for row in rows
        ]
    else:
        st.session_state.plants = []

# ─────────────────────────────────────────
# GİRİŞ PANELİ
# ─────────────────────────────────────────
if not st.session_state.logged_in:
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.write("")
        st.write("")
        st.title("🌿 Killi Bahçe")
        st.caption("Akıllı Bitki Bakım Asistanınız")
        st.divider()
        email    = st.text_input("E-posta",  placeholder="ornek@mail.com")
        password = st.text_input("Şifre",    placeholder="••••••••", type="password")
        if st.button("Giriş Yap", use_container_width=True):
            # TODO: DB'de kullanıcı tablosu oluşturulunca buraya gerçek auth gelecek
            if "@" in email:
                st.session_state.logged_in  = True
                st.session_state.user_email = email
                st.rerun()
            else:
                st.error("Geçerli bir e-posta girin.")
    st.stop()

# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.title("🌿 Killi Bahçe")
    st.caption(f"{len(st.session_state.plants)} Sağlıklı Bitki")
    st.divider()
    if st.button("🚪 Çıkış Yap"):
        st.session_state.logged_in = False
        st.rerun()

st.info("👈 Sol menüden bir sayfa seçin.")
