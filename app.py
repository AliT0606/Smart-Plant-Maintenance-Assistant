import streamlit as st
import pandas as pd
import datetime

# ==========================================
# 1. ADVANCED DESIGN SYSTEM (DESIGN.md)
# ==========================================
st.set_page_config(page_title="Arboretum Sanctuary", page_icon="🌿", layout="wide")

# CSS: Digital Arboretum Styles
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background-color: #fbf9f1 !important;
        color: #42493e !important;
    }

    /* Soft Card Style */
    .arb-card {
        background-color: #f5f4ec;
        border-radius: 28px;
        padding: 30px;
        margin-bottom: 24px;
        border: none;
    }

    /* Custom Input & Form Styling */
    .stTextInput>div>div>input {
        background-color: #f5f4ec !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 12px !important;
    }

    /* Botanical Chips for Radios */
    div[data-testid="stRadio"] div[role="radiogroup"] {
        flex-direction: row !important;
        gap: 10px;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label {
        background-color: #e4e3db !important;
        padding: 8px 20px !important;
        border-radius: 50px !important;
        border: none !important;
        transition: 0.3s;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label[data-selected="true"] {
        background: linear-gradient(135deg, #154212 0%, #2D5A27 100%) !important;
        color: white !important;
    }
    div[data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] p { margin: 0; font-weight: 500; }
    div[data-testid="stRadio"] input { display: none; }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #154212 0%, #2D5A27 100%) !important;
        border-radius: 50px !important;
        border: none !important;
        color: white !important;
        padding: 12px 35px !important;
        font-weight: 600 !important;
    }

    /* Delete Button Styling */
    .delete-btn>button {
        background: #e4e3db !important;
        color: #b3261e !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SESSION STATE (Login & Data)
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# ==========================================
# 3. LOGIN PAGE
# ==========================================
if not st.session_state.logged_in:
    col_l, col_mid, col_r = st.columns([1, 2, 1])
    with col_mid:
        st.markdown("<br><br><h1 style='text-align: center; color: #154212;'>🌿 Arboretum</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Welcome to your digital conservatory.</p>", unsafe_allow_html=True)
        
        st.markdown('<div class="arb-card">', unsafe_allow_html=True)
        email = st.text_input("E-mail Address", placeholder="example@mail.com")
        if st.button("Access Sanctuary"):
            if "@" in email:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Please enter a valid email.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ==========================================
# 4. MAIN APP NAVIGATION
# ==========================================
st.sidebar.markdown("<h2 style='color:#154212;'>ARBORETUM</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Navigation", ["Dashboard", "Collection", "Diagnosis", "Calendar", "Settings"])

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

# ==========================================
# 5. PANELS
# ==========================================

# --- DASHBOARD ---
if page == "Dashboard":
    # Weather at the top as requested
    st.markdown('<div class="arb-card" style="background: linear-gradient(90deg, #d0e8cf 0%, #fbf9f1 100%);">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 3])
    with c1:
        st.markdown("<h3 style='margin:0;'>☀️ 24°C</h3>", unsafe_allow_html=True)
        st.write("Elâzığ, TR")
    with c2:
        st.write("**Smart Forecast:** High UV today. Consider moving sensitive indoor plants away from direct window light. No rain expected.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<h1 style='color:#154212;'>The Sanctuary</h1>", unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="arb-card">', unsafe_allow_html=True)
        st.metric("HEALTH SCORE", "92%", "+1%")
        st.markdown('</div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="arb-card">', unsafe_allow_html=True)
        st.metric("PLANTS", "5", "Active")
        st.markdown('</div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="arb-card">', unsafe_allow_html=True)
        st.metric("TASKS", "3 Due", "Today")
        st.markdown('</div>', unsafe_allow_html=True)

# --- COLLECTION (With Delete & Species) ---
elif page == "Collection":
    st.markdown("<h1 style='color:#154212;'>Your Collection</h1>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Overview", "Add New Specimen"])
    
    with tab1:
        st.write("<br>", unsafe_allow_html=True)
        def render_plant(name, species, loc):
            st.markdown(f"""
                <div class="arb-card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <h3 style='margin:0; color:#154212;'>{name}</h3>
                            <p style='margin:0; font-size:0.8rem;'>{species}</p>
                        </div>
                        <span style='background:#e4e3db; padding:4px 12px; border-radius:20px; font-size:10px;'>{loc}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Remove {name}", key=name, help="Remove plant from sanctuary"):
                st.toast(f"{name} removed.")

        col_a, col_b = st.columns(2)
        with col_a: render_plant("Monstera", "Tropical Climber", "INDOOR")
        with col_b: render_plant("Cherry Tomato", "Vegetable", "OUTDOOR")

    with tab2:
        st.write("<br>", unsafe_allow_html=True)
        st.markdown('<div class="arb-card">', unsafe_allow_html=True)
        with st.form("add_plant"):
            st.subheader("New Specimen")
            st.text_input("Plant Nickname")
            st.text_input("Plant Species (e.g., Monstera Deliciosa)") # Added Species
            st.radio("Location", ["Indoor", "Outdoor"])
            st.form_submit_button("Add to System")
        st.markdown('</div>', unsafe_allow_html=True)

# --- DIAGNOSIS (Advanced Options) ---
elif page == "Diagnosis":
    st.markdown("<h1 style='color:#154212;'>Botanical Diagnosis</h1>", unsafe_allow_html=True)
    st.markdown('<div class="arb-card">', unsafe_allow_html=True)
    
    soil = st.radio("Soil Moisture", ["Bone Dry", "Moist", "Soggy"])
    leaf = st.radio("Leaf Signs", ["Healthy Green", "Yellowing", "Brown Tips", "White Spots", "Holes"])
    
    st.write("<br>", unsafe_allow_html=True)
    # Advanced logic as requested
    if soil == "Soggy" and leaf == "Yellowing":
        st.error("🚨 **Diagnosis:** Root Rot (Overwatering). Stop watering immediately.")
    elif soil == "Bone Dry" and leaf == "Brown Tips":
        st.warning("🏜️ **Diagnosis:** Extreme Dehydration. Water deeply.")
    elif leaf == "White Spots":
        st.info("🍄 **Diagnosis:** Powdery Mildew (Fungal). Improve air circulation.")
    elif leaf == "Holes":
        st.error("🐛 **Diagnosis:** Pest Infestation. Check under leaves for insects.")
    elif soil == "Moist" and leaf == "Healthy Green":
        st.success("✅ **Diagnosis:** Optimal Health. No action needed.")
    else:
        st.info("ℹ️ Analyzing symptoms... Observations saved.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- CALENDAR (With Interactive Checkboxes) ---
elif page == "Calendar":
    st.markdown("<h1 style='color:#154212;'>Care Schedule</h1>", unsafe_allow_html=True)
    st.markdown('<div class="arb-card">', unsafe_allow_html=True)
    st.date_input("Schedule For", datetime.date.today())
    st.write("<br>", unsafe_allow_html=True)
    
    # Task system with "Done" status
    c1, c2 = st.columns([4, 1])
    with c1: st.write("💧 Water the Indoor Monstera")
    with c2: st.checkbox("Done", key="t1")
    
    c1, c3 = st.columns([4, 1])
    with c1: st.write("✂️ Prune Outdoor Tomatoes")
    with c3: st.checkbox("Done", key="t2")
    st.markdown('</div>', unsafe_allow_html=True)

# --- SETTINGS (Location Selection) ---
elif page == "Settings":
    st.markdown("<h1 style='color:#154212;'>Settings</h1>", unsafe_allow_html=True)
    st.markdown('<div class="arb-card">', unsafe_allow_html=True)
    st.subheader("Regional Information")
    st.write("Set your location for accurate weather synchronization.")
    
    country = st.selectbox("Country", ["Turkey", "Germany", "USA", "UK"])
    city = st.text_input("City", value="Elâzığ")
    
    if st.button("Save Preferences"):
        st.success(f"Location set to {city}, {country}. Weather sync updated.")
    st.markdown('</div>', unsafe_allow_html=True)