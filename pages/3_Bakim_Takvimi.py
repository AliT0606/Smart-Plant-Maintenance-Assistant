import streamlit as st
import datetime

# ─────────────────────────────────────────
# LOGIN KONTROLÜ — düzeltildi
# ─────────────────────────────────────────
if not st.session_state.get("logged_in"):
    st.switch_page("app.py")

plants = st.session_state.get("plants", [])

# ─────────────────────────────────────────
# HAVA DURUMU İMPORT — hata olursa None döner
# ─────────────────────────────────────────
hava = None
try:
    from weather_service import hava_durumu_kontrol
    hava = hava_durumu_kontrol("Elazig")
except Exception:
    pass

# ─────────────────────────────────────────
# BAKIM TAKVİMİ
# ─────────────────────────────────────────
st.title("📅 Bakım Takvimi")
st.divider()

if "done_tasks" not in st.session_state:
    st.session_state.done_tasks = set()

if hava and hava["yagmur_var_mi"]:
    st.warning("🌧️ Bugün yağmur var — dış mekân sulama görevleri otomatik atlandı.")

col_tarih, col_filtre = st.columns([1, 2])
with col_tarih:
    tarih = st.date_input("Tarih", datetime.date.today())
with col_filtre:
    filtre = st.selectbox("Görev Türü", ["Tümü", "Sulama", "Gübre", "Kontrol", "Temizlik"])

st.divider()

IKONLAR = {"Sulama": "💧", "Gübre": "🌱", "Kontrol": "🔍", "Temizlik": "🍃"}
bugun   = datetime.date.today()

def gorev_olustur(plants, yagmur=False):
    gorevler = []
    for p in plants:
        dis_mekan = p["konum"] in ["Balkon", "Bahçe"]
        if p["sulama_periyodu"] <= 3:
            if not (yagmur and dis_mekan):
                gorevler.append({"bitki": p["ad"], "tur": "Sulama",   "tarih": bugun,                              "not": "Sulama zamanı geldi"})
        gorevler.append(        {"bitki": p["ad"], "tur": "Kontrol",  "tarih": bugun + datetime.timedelta(days=7), "not": "Genel sağlık kontrolü"})
        gorevler.append(        {"bitki": p["ad"], "tur": "Temizlik", "tarih": bugun + datetime.timedelta(days=1), "not": "Yaprak temizliği"})
        gorevler.append(        {"bitki": p["ad"], "tur": "Gübre",    "tarih": bugun + datetime.timedelta(days=3), "not": "Gübre zamanı"})
    return gorevler

yagmur_var   = hava["yagmur_var_mi"] if hava else False
tum_gorevler = gorev_olustur(plants, yagmur=yagmur_var)
if filtre != "Tümü":
    tum_gorevler = [g for g in tum_gorevler if g["tur"] == filtre]

gecmis   = [g for g in tum_gorevler if g["tarih"] <  bugun]
bugunler = [g for g in tum_gorevler if g["tarih"] == bugun]
gelecek  = [g for g in tum_gorevler if g["tarih"] >  bugun]

def gorev_listele(gorev_list, baslik):
    if not gorev_list:
        return
    st.subheader(baslik)
    for g in gorev_list:
        # Kararlı key: bitki + tür + tarih kombinasyonu (index kullanma)
        gid  = f"{g['bitki']}_{g['tur']}_{g['tarih']}"
        ikon = IKONLAR.get(g["tur"], "📌")
        with st.container(border=True):
            c1, c2 = st.columns([5, 1])
            with c1:
                tamamlandi = gid in st.session_state.done_tasks
                etiket = f"~~{ikon} **{g['bitki']}** — {g['tur']}~~" if tamamlandi else f"{ikon} **{g['bitki']}** — {g['tur']}"
                st.write(etiket)
                st.caption(f"{g['not']}  |  {g['tarih'].strftime('%d %b %Y')}")
            with c2:
                done = st.checkbox("Tamam", key=f"chk_{gid}", value=(gid in st.session_state.done_tasks))
                if done:
                    st.session_state.done_tasks.add(gid)
                else:
                    st.session_state.done_tasks.discard(gid)

gorev_listele(gecmis,   "🔴 Gecikmiş")
gorev_listele(bugunler, "🟢 Bugün")
gorev_listele(gelecek,  "🔵 Yaklaşan")

if not tum_gorevler:
    st.info("Bu filtre için görev bulunamadı.")

st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("Toplam Görev", len(tum_gorevler))
c2.metric("Tamamlanan",   len(st.session_state.done_tasks))
c3.metric("Bekleyen",     len(tum_gorevler) - len(st.session_state.done_tasks))
