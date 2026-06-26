import streamlit as st
st.set_page_config(page_title="Timing Optimization - CaffiSense", page_icon="☕", layout="wide")
from utils import init_session_state, compute_timing
init_session_state()

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.5rem; }
    .section-title { font-size: 1.3rem; font-weight: 600; color: #333; margin: 1.5rem 0 1rem; border-bottom: 2px solid #f0f0f0; padding-bottom: 0.5rem; }
    .time-card {
        background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 16px; padding: 1.5rem;
        text-align: center; color: white; box-shadow: 0 4px 20px rgba(102,126,234,0.2);
        height: 100%; display: flex; flex-direction: column; justify-content: center;
    }
    .time-value { font-size: 2rem; font-weight: 800; }
    .time-label { font-size: 0.85rem; opacity: 0.9; margin-bottom: 0.5rem; }
    .info-card { background: white; border-radius: 12px; padding: 1.2rem; border: 1px solid #f0f0f0; text-align: center; height: 100%; }
    .stButton > button { border-radius: 40px; font-weight: 600; padding: 0.5rem 2rem; width: 100%; }
</style>
""", unsafe_allow_html=True)

wake = st.session_state.wake_time
bed = st.session_state.bedtime
workout = st.session_state.workout_time

first_caf, prod_start, prod_end, pre_workout, last_safe = compute_timing(wake, bed, workout)

st.markdown('<div class="page-title">⏱ Timing Optimization</div>', unsafe_allow_html=True)
st.markdown('<p style="color:#666;">Optimized caffeine schedule based on your daily routine.</p>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Recommended Schedule</div>', unsafe_allow_html=True)

row1 = st.columns(4)
times = [
    ("First Caffeine", first_caf, "☕"),
    ("Productivity Window", f"{prod_start} - {prod_end}", "📊"),
    ("Pre-Workout", pre_workout, "💪"),
    ("Last Safe Time", last_safe, "⏰"),
]
for i, (label, val, icon) in enumerate(times):
    with row1[i]:
        st.markdown(f"""
        <div class="time-card">
            <div class="time-label">{icon} {label}</div>
            <div class="time-value">{val}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">Schedule Details</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="info-card">
        <div style="font-weight:600;color:#333;">Wake-Up Time</div>
        <div style="font-size:1.5rem;font-weight:700;color:#6b48ff;">{wake}</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="info-card">
        <div style="font-weight:600;color:#333;">Workout Time</div>
        <div style="font-size:1.5rem;font-weight:700;color:#6b48ff;">{workout}</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="info-card">
        <div style="font-weight:600;color:#333;">Bedtime</div>
        <div style="font-size:1.5rem;font-weight:700;color:#6b48ff;">{bed}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    if st.button("😴 Sleep Impact Analysis →", type="primary"):
        st.switch_page("pages/7_Sleep_Impact.py")
with col2:
    if st.button("📊 Analytics Dashboard →"):
        st.switch_page("pages/8_Analytics_Dashboard.py")

st.markdown("""
<div style="text-align:center;padding:2rem;color:#999;font-size:0.85rem;margin-top:2rem;">
    © 2026 CaffiSense
</div>
""", unsafe_allow_html=True)
