import streamlit as st
st.set_page_config(page_title="Caffeine Source - CaffiSense", page_icon="☕", layout="wide")
from utils import init_session_state, predict_caffeine
init_session_state()

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.5rem; }
    .section-title { font-size: 1.3rem; font-weight: 600; color: #333; margin: 1.5rem 0 1rem; border-bottom: 2px solid #f0f0f0; padding-bottom: 0.5rem; }
    .form-card { background: #fafafa; border-radius: 16px; padding: 2rem; border: 1px solid #f0f0f0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">☕ Caffeine Source Selection</div>', unsafe_allow_html=True)
st.markdown('<p style="color:#666;">Select the source of caffeine and provide details for accurate prediction.</p>', unsafe_allow_html=True)

source = st.selectbox(
    "Select Caffeine Source",
    options=["", "Coffee", "Tea", "Energy Drinks", "Soft Drinks", "Chocolates",
             "Cocoa Drinks", "Pre-Workout Drinks", "Caffeinated Sports Drinks", "Caffeine Tablets/Capsules"],
    index=0,
)
st.session_state.caffeine_source = source

if source:
    st.markdown('<div class="section-title">Source Details</div>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)

        if source == "Coffee":
            st.session_state.coffee_roast = st.radio("Roast Level", ["Light", "Medium", "Dark"],
                index=["Light", "Medium", "Dark"].index(st.session_state.coffee_roast), horizontal=True)
            st.session_state.brew_time = st.number_input("Brew Time (minutes)", min_value=1, max_value=15, value=st.session_state.brew_time)
            st.session_state.serving_size = st.number_input("Serving Size (ml)", min_value=30, max_value=600, value=st.session_state.serving_size)

        elif source == "Tea":
            st.session_state.tea_type = st.selectbox("Tea Type",
                ["Green Tea", "Black Tea", "Oolong Tea", "Herbal Tea", "Other"],
                index=["Green Tea", "Black Tea", "Oolong Tea", "Herbal Tea", "Other"].index(st.session_state.tea_type))
            st.session_state.brew_duration = st.number_input("Brewing Duration (minutes)", min_value=1, max_value=15, value=st.session_state.brew_duration)
            st.session_state.serving_size = st.number_input("Serving Size (ml)", min_value=30, max_value=600, value=st.session_state.serving_size)

        elif source in ["Energy Drinks", "Soft Drinks", "Pre-Workout Drinks", "Caffeinated Sports Drinks"]:
            st.session_state.brand_name = st.text_input("Brand Name", value=st.session_state.brand_name)
            st.session_state.serving_size = st.number_input("Serving Size (ml)", min_value=50, max_value=1000, value=st.session_state.serving_size)

        elif source == "Chocolates":
            st.session_state.chocolate_type = st.radio("Chocolate Type", ["Dark", "Milk", "White", "Other"],
                index=["Dark", "Milk", "White", "Other"].index(st.session_state.chocolate_type), horizontal=True)
            st.session_state.chocolate_weight = st.number_input("Weight (grams)", min_value=5, max_value=500, value=st.session_state.chocolate_weight)

        elif source == "Cocoa Drinks":
            st.session_state.serving_size = st.number_input("Serving Size (ml)", min_value=50, max_value=500, value=st.session_state.serving_size)

        elif source == "Caffeine Tablets/Capsules":
            st.session_state.tablet_dose = st.number_input("Dose Per Tablet (mg)", min_value=10, max_value=500, value=st.session_state.tablet_dose)
            st.session_state.tablet_qty = st.number_input("Quantity Consumed", min_value=1, max_value=20, value=st.session_state.tablet_qty)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔬 Analyze Caffeine", type="primary", use_container_width=True):
        mg = predict_caffeine(source, st.session_state)
        st.session_state.predicted_caffeine = mg
        st.session_state.source_label = source
        log = {
            'source': source,
            'mg': mg,
            'details': dict(st.session_state)
        }
        st.session_state.all_logs.append(log)
        st.switch_page("pages/3_AI_Prediction.py")

st.markdown("""
<div style="text-align:center;padding:2rem;color:#999;font-size:0.85rem;margin-top:2rem;">
    © 2026 CaffiSense
</div>
""", unsafe_allow_html=True)
