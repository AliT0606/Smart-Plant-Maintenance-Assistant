import streamlit as st

# ─────────────────────────────────────────
# SAYFA AYARLARI
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Bakım Asistanı",
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
# BACKEND İMPORT — hata olursa mock kullan
# ─────────────────────────────────────────
try:
    from database_handler import tum_bitkileri_getir
    DB_AKTIF = True
except Exception:
    DB_AKTIF = False

# ─────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Mock bitki verisi — yalnızca kullanıcının hiç bitkisi yoksa ilk açılışta kullanılır
MOCK_PLANTS = [
    {"id": 1, "ad": "Barış Çiçeği",  "tur": "Spathiphyllum",      "ekim_tarihi": "2024-01-15", "sulama_periyodu": 2,  "konum": "Salon",  "saglik": 85, "isik": "Dolaylı Güneş"},
    {"id": 2, "ad": "Sukulent",       "tur": "Echeveria",           "ekim_tarihi": "2024-02-20", "sulama_periyodu": 14, "konum": "Mutfak", "saglik": 95, "isik": "Tam Güneş"},
    {"id": 3, "ad": "Orkide",         "tur": "Phalaenopsis",        "ekim_tarihi": "2024-03-10", "sulama_periyodu": 7,  "konum": "Yatak",  "saglik": 70, "isik": "Dolaylı Güneş"},
    {"id": 4, "ad": "Para Çiçeği",    "tur": "Pilea peperomioides", "ekim_tarihi": "2024-04-05", "sulama_periyodu": 5,  "konum": "Ofis",   "saglik": 90, "isik": "Parlak Dolaylı"},
    {"id": 5, "ad": "Pothos",         "tur": "Epipremnum aureum",   "ekim_tarihi": "2024-05-01", "sulama_periyodu": 7,  "konum": "Banyo",  "saglik": 88, "isik": "Az Işık"},
]

# plants session'da yoksa yükle (sayfa yenilemede tekrar yükleme yapma)
if "plants" not in st.session_state:
    loaded = False
    if DB_AKTIF:
        from perenual_service import bitki_bilgisi_getir
        try:
            rows = tum_bitkileri_getir()
            if rows:
                yeni_bitkiler = []
                for row in rows:
                    tur = row[2]
                    db_periyot = row[4]
                    
                    # Işık verisi veritabanında olmadığı için anlık olarak Mock sistemden alıyoruz
                    api_veri = bitki_bilgisi_getir(tur)
                    isik_verisi = api_veri["isik"] if api_veri else "Bilinmiyor"
                    
                    # Eğer daha önceden veritabanına hatalı kaydedilmiş 7 günlük eski bir bitkiyse, onu da düzeltiyoruz
                    gercek_periyot = api_veri["periyot_gun"] if api_veri and db_periyot == 7 else db_periyot

                    yeni_bitkiler.append({
                        "id":             row[0],
                        "ad":             row[1],
                        "tur":            tur,
                        "ekim_tarihi":    row[3],
                        "sulama_periyodu":gercek_periyot,
                        "konum":          row[5],
                        "saglik":         80,
                        "isik":           isik_verisi,
                    })
                st.session_state.plants = yeni_bitkiler
                loaded = True
        except Exception as e:
            print("DB çekme hatası:", e)
            pass
    # DB yoksa veya boşsa: mock sadece ilk açılışta
    if not loaded:
        st.session_state.plants = MOCK_PLANTS

if "db_aktif" not in st.session_state:
    st.session_state.db_aktif = DB_AKTIF

# ─────────────────────────────────────────
# GİRİŞ PANELİ
# ─────────────────────────────────────────
if not st.session_state.logged_in:
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.write("")
        st.write("")
        st.title("🌿 Bakım Asistanı")
        st.caption("Akıllı Bitki Bakım Asistanınız")
        st.divider()
        email    = st.text_input("E-posta",  placeholder="ornek@mail.com")
        password = st.text_input("Şifre",    placeholder="••••••••", type="password")
        if st.button("Giriş Yap", use_container_width=True):
            if "@" in email:
                st.session_state.logged_in  = True
                st.session_state.user_email = email
                st.rerun()
            else:
                st.error("Geçerli bir e-posta girin.")
        st.caption("Demo: herhangi @ içeren e-posta ile giriş yapabilirsiniz.")
    st.stop()

# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.title("🌿 Bakım Asistanı ")
    st.caption(f"{len(st.session_state.plants)} Sağlıklı Bitki")
    st.divider()
    if not st.session_state.db_aktif:
        st.warning("⚠️ DB bağlantısı yok\nMock veri kullanılıyor.")
    st.divider()
    if st.button("🚪 Çıkış Yap"):
        st.session_state.logged_in = False
        st.rerun()

st.info("👈 Sol menüden bir sayfa seçin.")
