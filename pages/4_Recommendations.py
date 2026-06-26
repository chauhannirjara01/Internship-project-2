import streamlit as st
st.set_page_config(page_title="Recommendations - CaffiSense", page_icon="☕", layout="wide")
from utils import init_session_state, get_recommendations
init_session_state()

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.5rem; }
    .section-title { font-size: 1.3rem; font-weight: 600; color: #333; margin: 1.5rem 0 1rem; border-bottom: 2px solid #f0f0f0; padding-bottom: 0.5rem; }
    .stat-card { background: white; border-radius: 16px; padding: 1.5rem; border: 1px solid #f0f0f0; text-align: center; height: 100%; }
    .stat-value { font-size: 2rem; font-weight: 800; color: #6b48ff; }
    .stat-label { color: #666; font-size: 0.9rem; margin-top: 0.3rem; }
    .rec-card { background: #f8f6ff; border-left: 4px solid #6b48ff; border-radius: 12px; padding: 1.2rem; margin: 0.8rem 0; }
    .stButton > button { border-radius: 40px; font-weight: 600; padding: 0.5rem 2rem; width: 100%; }
    .overview-item { display: flex; justify-content: space-between; padding: 0.5rem 0; border-bottom: 1px solid #f5f5f5; }
</style>
""", unsafe_allow_html=True)

age = st.session_state.age
weight = st.session_state.weight
sensitivity = st.session_state.sensitivity
conditions = st.session_state.health_conditions
mg = st.session_state.predicted_caffeine

daily_limit, recs = get_recommendations(age, weight, sensitivity, conditions)

st.markdown('<div class="page-title">📋 Personalized Recommendation Dashboard</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown(f"""
    <div class="stat-card">
        <div style="font-weight:600;margin-bottom:0.8rem;">User Overview</div>
        <div class="overview-item"><span>Age:</span><span>{age}</span></div>
        <div class="overview-item"><span>Weight:</span><span>{weight} kg</span></div>
        <div class="overview-item"><span>Sensitivity:</span><span>{sensitivity}</span></div>
        <div class="overview-item"><span>Health:</span><span>{', '.join(conditions) if conditions else 'None'}</span></div>
        <div class="overview-item"><span>Workout:</span><span>{st.session_state.workout_time}</span></div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-label">Recommended Daily Intake</div>
        <div class="stat-value">{daily_limit} mg/day</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    remaining = max(0, daily_limit - mg)
    pct = min(100, int(mg / daily_limit * 100))
    bar_color = "#22c55e" if pct < 50 else ("#eab308" if pct < 80 else "#ef4444")
    st.markdown(f"""
    <div class="stat-card">
        <div style="font-size:1.1rem;font-weight:700;">{mg} mg Consumed</div>
        <div style="font-size:0.9rem;color:#666;">{remaining} mg Remaining</div>
        <div style="height:8px;border-radius:20px;background:#f0f0f0;margin-top:0.8rem;overflow:hidden;">
            <div style="height:100%;width:{pct}%;background:{bar_color};border-radius:20px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    st.markdown('<div style="font-weight:600;margin-bottom:0.8rem;">AI Recommendation Panel</div>', unsafe_allow_html=True)
    for r in recs:
        st.markdown(f'<div class="rec-card">💡 {r}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    if st.button("🏥 Health Analysis →", type="primary"):
        st.switch_page("pages/5_Health_Analysis.py")
with col2:
    if st.button("⏱ Timing Optimization →"):
        st.switch_page("pages/6_Timing_Optimization.py")

st.markdown("""
<div style="text-align:center;padding:2rem;color:#999;font-size:0.85rem;margin-top:2rem;">
    © 2026 CaffiSense
</div>
""", unsafe_allow_html=True)
