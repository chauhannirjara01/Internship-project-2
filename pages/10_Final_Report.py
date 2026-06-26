import streamlit as st
st.set_page_config(page_title="Final Report - CaffiSense", page_icon="☕", layout="wide")
from utils import init_session_state, get_recommendations, compute_timing, compute_sleep_impact
init_session_state()

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.5rem; }
    .section-title { font-size: 1.3rem; font-weight: 600; color: #333; margin: 1.5rem 0 1rem; border-bottom: 2px solid #f0f0f0; padding-bottom: 0.5rem; }
    .report-card { background: white; border-radius: 16px; padding: 1.5rem; border: 1px solid #f0f0f0; height: 100%; }
    .summary-item { display: flex; justify-content: space-between; padding: 0.5rem 0; border-bottom: 1px solid #f5f5f5; }
    .stButton > button { border-radius: 40px; font-weight: 600; padding: 0.5rem 2rem; width: 100%; }
    .download-section { background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 20px; padding: 2rem; color: white; text-align: center; }
</style>
""", unsafe_allow_html=True)

age = st.session_state.age
weight = st.session_state.weight
sensitivity = st.session_state.sensitivity
conditions = st.session_state.health_conditions
mg = st.session_state.predicted_caffeine
source = st.session_state.source_label

daily_limit, recs = get_recommendations(age, weight, sensitivity, conditions)
first_caf, prod_start, prod_end, pre_workout, last_safe = compute_timing(
    st.session_state.wake_time, st.session_state.bedtime, st.session_state.workout_time)
score, remaining, _ = compute_sleep_impact(mg, st.session_state.bedtime)

st.markdown('<div class="page-title">📋 Final Report</div>', unsafe_allow_html=True)
st.markdown('<p style="color:#666;">Comprehensive summary of your caffeine analysis.</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="section-title">User Summary</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="report-card">
        <div class="summary-item"><span>Age</span><span>{age}</span></div>
        <div class="summary-item"><span>Weight</span><span>{weight} kg</span></div>
        <div class="summary-item"><span>Sensitivity</span><span>{sensitivity}</span></div>
        <div class="summary-item"><span>Wake-up</span><span>{st.session_state.wake_time}</span></div>
        <div class="summary-item"><span>Bedtime</span><span>{st.session_state.bedtime}</span></div>
        <div class="summary-item"><span>Workout</span><span>{st.session_state.workout_time}</span></div>
        <div class="summary-item"><span>Conditions</span><span>{', '.join(conditions) if conditions else 'None'}</span></div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown('<div class="section-title">Caffeine Analysis</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="report-card">
        <div class="summary-item"><span>Source</span><span>{source or 'N/A'}</span></div>
        <div class="summary-item"><span>Predicted Caffeine</span><span><strong>{mg} mg</strong></span></div>
        <div class="summary-item"><span>Daily Limit</span><span>{daily_limit} mg</span></div>
        <div class="summary-item"><span>Remaining</span><span>{max(0, daily_limit - mg)} mg</span></div>
        <div style="margin-top:1rem;padding:0.5rem;background:#f8f6ff;border-radius:8px;">
            <div style="font-weight:600;color:#6b48ff;">Best Consumption Time: {first_caf}</div>
            <div style="font-weight:600;color:#6b48ff;">Last Safe Time: {last_safe}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown('<div class="section-title">Recommendations</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="report-card">
        <div class="summary-item"><span>Daily Limit</span><span>{daily_limit} mg/day</span></div>
        <div class="summary-item"><span>Best Time</span><span>{first_caf}</span></div>
        <div class="summary-item"><span>Last Safe</span><span>{last_safe}</span></div>
        <div class="summary-item"><span>Sleep Score</span><span style="color:{'#22c55e' if score == 'GREEN' else '#eab308' if score == 'YELLOW' else '#ef4444'};font-weight:700;">{score}</span></div>
        <div style="margin-top:1rem;">
            <div style="font-size:0.9rem;color:#666;">Sleep Impact</div>
            <div style="font-weight:600;">{remaining} mg estimated at bedtime</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">AI Recommendations</div>', unsafe_allow_html=True)
for r in recs:
    st.markdown(f'<div style="background:#f8f6ff;border-left:4px solid #6b48ff;border-radius:8px;padding:0.8rem 1rem;margin:0.4rem 0;">💡 {r}</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">Download & Export</div>', unsafe_allow_html=True)
st.markdown("""
<div class="download-section">
    <div style="font-size:1.5rem;font-weight:700;margin-bottom:0.5rem;">Download Your Report</div>
    <p style="opacity:0.9;margin-bottom:1.5rem;">Save your caffeine analysis report for future reference.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    report_text = f"""CAFFISENSE - FINAL REPORT
========================
Profile: Age {age}, Weight {weight}kg, Sensitivity {sensitivity}
Conditions: {', '.join(conditions) if conditions else 'None'}
Source: {source}
Predicted Caffeine: {mg} mg
Daily Limit: {daily_limit} mg/day
Best Time: {first_caf}
Last Safe: {last_safe}
Sleep Score: {score}
"""
    st.download_button("📄 Download PDF Report", data=report_text, file_name="caffisense_report.txt", mime="text/plain")
with col2:
    st.download_button("📊 Export Data", data=report_text, file_name="caffisense_data.txt", mime="text/plain")
with col3:
    if st.button("💾 Save Analysis"):
        st.success("Analysis saved successfully!")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🏠 Back to Home", type="primary", use_container_width=True):
    st.switch_page("app.py")

st.markdown("""
<div style="text-align:center;padding:2rem;color:#999;font-size:0.85rem;margin-top:2rem;">
    © 2026 CaffiSense — Thank you for using our platform
</div>
""", unsafe_allow_html=True)
