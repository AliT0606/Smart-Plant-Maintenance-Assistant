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

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background-color: #f5f0e8 !important;
    color: #2a2e27 !important;
}
section[data-testid="stSidebar"] { background-color: #ede8dd !important; }
.stButton > button {
    background: linear-gradient(135deg, #1a3a1a, #2d5a27) !important;
    color: #fff !important; border: none !important;
    border-radius: 50px !important; font-weight: 600 !important;
}
.stTextInput > div > div > input {
    background-color: #edeade !important;
    border-radius: 12px !important; border: 1.5px solid #ccc8bc !important;
}
[data-testid="metric-container"] {
    background: #edeade; border-radius: 16px; padding: 14px 18px;
}
.stTabs [data-baseweb="tab"] { border-radius: 50px !important; font-weight: 500 !important; }
.stTabs [aria-selected="true"] { background: #1a3a1a !important; color: #fff !important; }
.stProgress > div > div > div { background: #2d5a27 !important; border-radius: 99px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# DİL TANIMLAMALARI
# ─────────────────────────────────────────
DILLER = {
    "🇹🇷 Türkçe": {
        "baslik":    "Bakım Asistanı",
        "giris":     "Giriş Yap",
        "eposta":    "E-posta",
        "sifre":     "Şifre",
        "cikis":     "🚪 Çıkış Yap",
        "saglikli":  "Sağlıklı Bitki",
        "db_uyari":  "⚠️ DB bağlantısı yok",
        "sayfa_sec": "👈 Sol menüden bir sayfa seçin.",
        "demo":      "Demo: herhangi @ içeren e-posta ile giriş yapabilirsiniz.",
        "dil":       "🌐 Dil / Language",
        "sayfalar":  ["🌿 Panel", "📚 Kütüphane", "📅 Takvim", "📊 İstatistikler", "🔬 Teşhis"],
    },
    "🇬🇧 English": {
        "baslik":    "Plant Care Assistant",
        "giris":     "Login",
        "eposta":    "Email",
        "sifre":     "Password",
        "cikis":     "🚪 Logout",
        "saglikli":  "Healthy Plants",
        "db_uyari":  "⚠️ No DB connection",
        "sayfa_sec": "👈 Select a page from the left menu.",
        "demo":      "Demo: any email with @ works.",
        "dil":       "🌐 Dil / Language",
        "sayfalar":  ["🌿 Dashboard", "📚 Library", "📅 Calendar", "📊 Statistics", "🔬 Diagnosis"],
    }
}

# ─────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────
if "dil" not in st.session_state:
    st.session_state.dil = "🇹🇷 Türkçe"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

T = DILLER[st.session_state.dil]

# ─────────────────────────────────────────
# BACKEND İMPORT
# ─────────────────────────────────────────
try:
    from database_handler import tum_bitkileri_getir, saglik_hesapla, tamamlanan_gorevleri_getir
    DB_AKTIF = True
except Exception as e:
    print("DB import hatası:", e)
    DB_AKTIF = False

# ─────────────────────────────────────────
# BİTKİLERİ YÜKLE
# ─────────────────────────────────────────
if "plants" not in st.session_state:
    if DB_AKTIF:
        try:
            from perenual_service import bitki_bilgisi_getir
            rows = tum_bitkileri_getir()
            yeni_bitkiler = []
            for row in rows:
                tur        = row[2]
                db_periyot = row[4]
                son_sulama = row[7]
                api_veri   = bitki_bilgisi_getir(tur)
                isik       = api_veri["isik"] if api_veri else "Bilinmiyor"
                # Artık kafasına göre hesaplamayacak, veritabanındaki gerçek sağlığı (row[6]) alacak
                saglik     = row[6] if row[6] is not None else 80
                yeni_bitkiler.append({
                    "id": row[0], "ad": row[1], "tur": tur,
                    "ekim_tarihi": row[3], "sulama_periyodu": db_periyot,
                    "konum": row[5], "saglik": saglik, "isik": isik,
                    "son_sulama": str(son_sulama) if son_sulama else None,
                })
            st.session_state.plants = yeni_bitkiler
        except Exception as e:
            print("Bitki yükleme hatası:", e)
            st.session_state.plants = []
    else:
        st.session_state.plants = []

if "db_aktif" not in st.session_state:
    st.session_state.db_aktif = DB_AKTIF

if "done_tasks" not in st.session_state:
    if DB_AKTIF:
        try:
            st.session_state.done_tasks = tamamlanan_gorevleri_getir()
        except Exception:
            st.session_state.done_tasks = set()
    else:
        st.session_state.done_tasks = set()

# ─────────────────────────────────────────
# GİRİŞ PANELİ
# ─────────────────────────────────────────
if not st.session_state.logged_in:
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.write(""); st.write("")
        st.title(f"🌿 {T['baslik']}")
        st.caption("Akıllı Bitki Bakım Asistanınız" if st.session_state.dil == "🇹🇷 Türkçe" else "Smart Plant Care Assistant")
        st.divider()
        dil_sec = st.selectbox(T["dil"], list(DILLER.keys()), index=list(DILLER.keys()).index(st.session_state.dil))
        if dil_sec != st.session_state.dil:
            st.session_state.dil = dil_sec
            st.rerun()
        email    = st.text_input(T["eposta"], placeholder="ornek@mail.com")
        password = st.text_input(T["sifre"],  placeholder="••••••••", type="password")
        if st.button(T["giris"], use_container_width=True):
            if "@" in email:
                st.session_state.logged_in  = True
                st.session_state.user_email = email
                st.rerun()
            else:
                st.error("Geçerli bir e-posta girin." if st.session_state.dil == "🇹🇷 Türkçe" else "Enter a valid email.")
        st.caption(T["demo"])
    st.stop()

# ─────────────────────────────────────────
# NAVIGATION — sidebar sayfa isimleri dile göre değişir
# ─────────────────────────────────────────
isimler = T["sayfalar"]

sayfalar = st.navigation({
    f"🌿 {T['baslik']}": [
        st.Page("pages/1_Dashboard.py",          title=isimler[0], icon="🌿"),
        st.Page("pages/2_Bitki_Kutuphanesi.py",  title=isimler[1], icon="📚"),
        st.Page("pages/3_Bakim_Takvimi.py",      title=isimler[2], icon="📅"),
        st.Page("pages/4_Istatistikler.py",      title=isimler[3], icon="📊"),
        st.Page("pages/5_Hasta_Bitki_Teshis.py", title=isimler[4], icon="🔬"),
    ]
})

# ─────────────────────────────────────────
# SIDEBAR — çıkış + dil
# ─────────────────────────────────────────
with st.sidebar:
    st.divider()
    dil_sec = st.selectbox(T["dil"], list(DILLER.keys()), index=list(DILLER.keys()).index(st.session_state.dil), key="sidebar_dil")
    if dil_sec != st.session_state.dil:
        st.session_state.dil = dil_sec
        st.rerun()
    st.caption(f"{len(st.session_state.plants)} {T['saglikli']}")
    if not st.session_state.db_aktif:
        st.warning(T["db_uyari"])
    st.divider()
    if st.button(T["cikis"]):
        st.session_state.logged_in = False
        st.rerun()

sayfalar.run()