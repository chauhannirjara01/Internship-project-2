import streamlit as st
st.set_page_config(page_title="Sleep Impact - CaffiSense", page_icon="☕", layout="wide")
from utils import init_session_state, compute_sleep_impact
init_session_state()

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.5rem; }
    .section-title { font-size: 1.3rem; font-weight: 600; color: #333; margin: 1.5rem 0 1rem; border-bottom: 2px solid #f0f0f0; padding-bottom: 0.5rem; }
    .score-card { border-radius: 20px; padding: 3rem; text-align: center; color: white; box-shadow: 0 10px 40px rgba(0,0,0,0.1); }
    .score-value { font-size: 3rem; font-weight: 800; }
    .score-label { font-size: 1.1rem; opacity: 0.9; }
    .info-card { background: white; border-radius: 16px; padding: 1.5rem; border: 1px solid #f0f0f0; text-align: center; height: 100%; }
    .warn-card { background: #fef2f2; border-left: 4px solid #ef4444; border-radius: 12px; padding: 1.2rem; margin: 1rem 0; }
    .stButton > button { border-radius: 40px; font-weight: 600; padding: 0.5rem 2rem; width: 100%; }
</style>
""", unsafe_allow_html=True)

mg = st.session_state.predicted_caffeine
bed = st.session_state.bedtime

score, remaining, hrs = compute_sleep_impact(mg, bed)

color_map = {"GREEN": "#22c55e", "YELLOW": "#eab308", "RED": "#ef4444"}
bg_map = {"GREEN": "linear-gradient(135deg, #22c55e, #16a34a)",
          "YELLOW": "linear-gradient(135deg, #eab308, #ca8a04)",
          "RED": "linear-gradient(135deg, #ef4444, #dc2626)"}

st.markdown('<div class="page-title">😴 Sleep Impact Analysis</div>', unsafe_allow_html=True)
st.markdown('<p style="color:#666;">Understand how your caffeine consumption affects your sleep quality.</p>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 2])
with col1:
    st.markdown(f"""
    <div class="score-card" style="background:{bg_map[score]};">
        <div class="score-label">Sleep Impact Score</div>
        <div class="score-value">{score}</div>
        <div style="margin-top:1rem;opacity:0.8;">
            {"✅ Low impact on sleep" if score == "GREEN" else "⚠️ Moderate impact" if score == "YELLOW" else "🔴 High risk of sleep disruption"}
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="info-card">
        <div style="font-weight:600;margin-bottom:1rem;">Remaining Caffeine Estimation</div>
        <div style="font-size:1rem;color:#666;">Caffeine Consumed: <strong>{mg} mg</strong></div>
        <div style="font-size:1rem;color:#666;margin:0.5rem 0;">Hours until bedtime: <strong>{hrs}h</strong></div>
        <div style="margin:1.5rem 0;">
            <div style="font-size:0.9rem;color:#999;">Estimated Remaining at Bedtime</div>
            <div style="font-size:2.5rem;font-weight:800;color:{color_map[score]};">{remaining} mg</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if score != "GREEN":
    st.markdown("""
    <div class="warn-card">
        <div style="display:flex;align-items:center;gap:0.5rem;">
            <span style="font-size:1.5rem;">⚠</span>
            <span style="font-weight:700;color:#991b1b;">Sleep Warning</span>
        </div>
        <div style="color:#666;margin-top:0.5rem;">
            Consuming caffeine after 5 PM may negatively affect sleep quality. Consider adjusting your intake timing.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📊 Analytics Dashboard →", type="primary"):
        st.switch_page("pages/8_Analytics_Dashboard.py")
with col2:
    if st.button("🔔 View Alerts →"):
        st.switch_page("pages/9_Alerts.py")
with col3:
    if st.button("📋 Final Report →"):
        st.switch_page("pages/10_Final_Report.py")

st.markdown("""
<div style="text-align:center;padding:2rem;color:#999;font-size:0.85rem;margin-top:2rem;">
    © 2026 CaffiSense
</div>
""", unsafe_allow_html=True)
