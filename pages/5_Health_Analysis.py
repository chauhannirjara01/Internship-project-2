import streamlit as st
st.set_page_config(page_title="Health Analysis - CaffiSense", page_icon="☕", layout="wide")
from utils import init_session_state, HEALTH_WARNINGS
init_session_state()

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.5rem; }
    .section-title { font-size: 1.3rem; font-weight: 600; color: #333; margin: 1.5rem 0 1rem; border-bottom: 2px solid #f0f0f0; padding-bottom: 0.5rem; }
    .health-card { background: white; border-radius: 16px; padding: 1.5rem; border: 1px solid #f0f0f0; margin-bottom: 1rem; }
    .detected-badge { display: inline-block; background: #dcfce7; color: #166534; padding: 0.3rem 1rem; border-radius: 20px; font-weight: 600; margin: 0.2rem; }
    .warning-card { border-left: 4px solid #eab308; background: #fffbeb; border-radius: 12px; padding: 1rem; margin: 0.5rem 0; }
    .stButton > button { border-radius: 40px; font-weight: 600; padding: 0.5rem 2rem; width: 100%; }
</style>
""", unsafe_allow_html=True)

conditions = st.session_state.health_conditions

st.markdown('<div class="page-title">🏥 Health Analysis Section</div>', unsafe_allow_html=True)
st.markdown('<p style="color:#666;">Health-aware insights based on your profile conditions.</p>', unsafe_allow_html=True)

if conditions:
    st.markdown('<div class="section-title">Health Conditions Detected</div>', unsafe_allow_html=True)
    tags = " ".join([f'<span class="detected-badge">✓ {c}</span>' for c in conditions])
    st.markdown(f'<div>{tags}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Health Warnings</div>', unsafe_allow_html=True)
    for c in conditions:
        warning = HEALTH_WARNINGS.get(c, "Monitor your caffeine intake.")
        st.markdown(f"""
        <div class="warning-card">
            <div style="font-weight:700;color:#92400e;font-size:1.1rem;">⚠ {c}</div>
            <div style="color:#666;margin-top:0.3rem;">{warning}</div>
        </div>
        """, unsafe_allow_html=True)

    for c in conditions:
        if c not in HEALTH_WARNINGS:
            st.markdown(f"""
            <div class="warning-card">
                <div style="font-weight:700;color:#92400e;">⚠ {c}</div>
                <div style="color:#666;margin-top:0.3rem;">Consult your healthcare provider for personalized advice regarding {c.lower()}.</div>
            </div>
            """, unsafe_allow_html=True)
else:
    st.markdown('<div class="section-title">Health Status</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="health-card" style="text-align:center;padding:2rem;">
        <div style="font-size:3rem;">✅</div>
        <div style="font-size:1.2rem;font-weight:600;color:#166534;">No Health Conditions Detected</div>
        <div style="color:#666;margin-top:0.5rem;">Your profile shows no health conditions that interact with caffeine.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    if st.button("⏱ Timing Optimization →", type="primary"):
        st.switch_page("pages/6_Timing_Optimization.py")
with col2:
    if st.button("😴 Sleep Impact →"):
        st.switch_page("pages/7_Sleep_Impact.py")

st.markdown("""
<div style="text-align:center;padding:2rem;color:#999;font-size:0.85rem;margin-top:2rem;">
    © 2026 CaffiSense
</div>
""", unsafe_allow_html=True)
