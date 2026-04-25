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
# GLOBAL TEMA  (sadece renk + font, HTML yok)
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
# SESSION STATE
# ─────────────────────────────────────────
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Mock bitki verisi (backend olmadan test için)
if "plants" not in st.session_state:
    st.session_state.plants = [
        {"ad": "Barış Çiçeği",  "tur": "Spathiphyllum",       "konum": "Salon",   "sulama_periyodu": 2,  "saglik": 85, "isik": "Dolaylı Güneş"},
        {"ad": "Sukulent",      "tur": "Echeveria",            "konum": "Mutfak",  "sulama_periyodu": 14, "saglik": 95, "isik": "Tam Güneş"},
        {"ad": "Orkide",        "tur": "Phalaenopsis",         "konum": "Yatak",   "sulama_periyodu": 7,  "saglik": 70, "isik": "Dolaylı Güneş"},
        {"ad": "Para Çiçeği",   "tur": "Pilea peperomioides",  "konum": "Ofis",    "sulama_periyodu": 5,  "saglik": 90, "isik": "Parlak Dolaylı"},
        {"ad": "Pothos",        "tur": "Epipremnum aureum",    "konum": "Banyo",   "sulama_periyodu": 7,  "saglik": 88, "isik": "Az Işık"},
    ]

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
        email    = st.text_input("E-posta", placeholder="ornek@mail.com")
        password = st.text_input("Şifre",   placeholder="••••••••", type="password")
        if st.button("Giriş Yap", use_container_width=True):
            if "@" in email:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.rerun()
            else:
                st.error("Geçerli bir e-posta girin.")
        st.caption("Demo: herhangi @ içeren e-posta ile giriş yapabilirsiniz.")
    st.stop()

# ─────────────────────────────────────────
# SIDEBAR — çıkış butonu
# ─────────────────────────────────────────
with st.sidebar:
    st.title("🌿 Killi Bahçe")
    st.caption(f"{len(st.session_state.plants)} Sağlıklı Bitki")
    st.divider()
    if st.button("🚪 Çıkış Yap"):
        st.session_state.logged_in = False
        st.rerun()

# Ana sayfa yönlendirme mesajı (pages/ otomatik çalışır)
st.info("👈 Sol menüden bir sayfa seçin.")
