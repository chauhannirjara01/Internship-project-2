import streamlit as st
st.set_page_config(page_title="AI Prediction - CaffiSense", page_icon="☕", layout="wide")
from utils import init_session_state
init_session_state()

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.5rem; }
    .result-card {
        background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 20px; padding: 3rem;
        text-align: center; color: white; box-shadow: 0 10px 40px rgba(102,126,234,0.3);
    }
    .result-mg { font-size: 4rem; font-weight: 800; }
    .result-label { font-size: 1.2rem; opacity: 0.9; }
    .detail-card { background: white; border-radius: 16px; padding: 1.5rem; border: 1px solid #f0f0f0; }
    .risk-bar { height: 12px; border-radius: 20px; background: #f0f0f0; overflow: hidden; margin: 1rem 0; }
    .risk-fill { height: 100%; border-radius: 20px; transition: width 0.5s; }
    .stButton > button { border-radius: 40px; font-weight: 600; padding: 0.5rem 2rem; width: 100%; }
</style>
""", unsafe_allow_html=True)

mg = st.session_state.predicted_caffeine
source = st.session_state.source_label

st.markdown('<div class="page-title">🔬 AI Prediction Results</div>', unsafe_allow_html=True)
st.markdown('<p style="color:#666;">Our AI model has analyzed your caffeine source and predicted the caffeine content.</p>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">Predicted Caffeine</div>
        <div class="result-mg">{mg} mg</div>
        <div style="margin-top:1rem;opacity:0.8;">per serving</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    if mg <= 100:
        risk = "Low Risk"
        color = "#22c55e"
        pct = 33
    elif mg <= 250:
        risk = "Moderate Risk"
        color = "#eab308"
        pct = 66
    else:
        risk = "High Risk"
        color = "#ef4444"
        pct = 100
    st.markdown(f"""
    <div class="detail-card">
        <div style="font-weight:600;margin-bottom:1rem;">Risk Indicator</div>
        <div style="font-size:1.2rem;font-weight:700;color:{color};">{risk}</div>
        <div class="risk-bar"><div class="risk-fill" style="width:{pct}%;background:{color};"></div></div>
        <div style="display:flex;justify-content:space-between;font-size:0.8rem;color:#999;">
            <span>Low Risk</span><span>Moderate</span><span>High Risk</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    details = []
    if source == "Coffee":
        details.append(f"Roast: {st.session_state.coffee_roast}")
        details.append(f"Serving: {st.session_state.serving_size} ml")
        details.append(f"Brew Time: {st.session_state.brew_time} min")
    elif source == "Tea":
        details.append(f"Type: {st.session_state.tea_type}")
        details.append(f"Serving: {st.session_state.serving_size} ml")
        details.append(f"Brew Duration: {st.session_state.brew_duration} min")
    elif source in ["Energy Drinks", "Soft Drinks", "Pre-Workout Drinks", "Caffeinated Sports Drinks"]:
        details.append(f"Brand: {st.session_state.brand_name or 'N/A'}")
        details.append(f"Serving: {st.session_state.serving_size} ml")
    elif source == "Chocolates":
        details.append(f"Type: {st.session_state.chocolate_type}")
        details.append(f"Weight: {st.session_state.chocolate_weight}g")
    elif source == "Caffeine Tablets/Capsules":
        details.append(f"Dose: {st.session_state.tablet_dose} mg/tablet")
        details.append(f"Quantity: {st.session_state.tablet_qty}")
    st.markdown(f"""
    <div class="detail-card">
        <div style="font-weight:600;margin-bottom:0.5rem;">Source Summary</div>
        <div style="font-size:1.1rem;font-weight:700;">{source}</div>
        {"<br>".join(f"<span style='color:#666;'>{d}</span>" for d in details)}
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("✨ Generate Recommendations", type="primary", use_container_width=True):
    st.switch_page("pages/4_Recommendations.py")

st.markdown("""
<div style="text-align:center;padding:2rem;color:#999;font-size:0.85rem;margin-top:2rem;">
    © 2026 CaffiSense
</div>
""", unsafe_allow_html=True)
