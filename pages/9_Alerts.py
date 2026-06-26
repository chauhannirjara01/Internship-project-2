import streamlit as st
st.set_page_config(page_title="Alerts - CaffiSense", page_icon="☕", layout="wide")
from utils import init_session_state, get_recommendations
init_session_state()

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.5rem; }
    .section-title { font-size: 1.3rem; font-weight: 600; color: #333; margin: 1.5rem 0 1rem; border-bottom: 2px solid #f0f0f0; padding-bottom: 0.5rem; }
    .alert-card { border-radius: 16px; padding: 1.5rem; margin: 1rem 0; display: flex; align-items: flex-start; gap: 1rem; }
    .alert-icon { font-size: 2rem; }
    .alert-title { font-weight: 700; font-size: 1.1rem; }
    .alert-desc { color: #666; margin-top: 0.3rem; }
    .red-alert { background: #fef2f2; border: 1px solid #fecaca; border-left: 4px solid #ef4444; }
    .yellow-alert { background: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid #eab308; }
    .green-alert { background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 4px solid #22c55e; }
    .stButton > button { border-radius: 40px; font-weight: 600; padding: 0.5rem 2rem; width: 100%; }
</style>
""", unsafe_allow_html=True)

daily_limit, _ = get_recommendations(st.session_state.age, st.session_state.weight, st.session_state.sensitivity, st.session_state.health_conditions)
mg = st.session_state.predicted_caffeine

st.markdown('<div class="page-title">🔔 Alerts & Notifications</div>', unsafe_allow_html=True)
st.markdown('<p style="color:#666;">Real-time alerts about your caffeine intake status.</p>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Current Alerts</div>', unsafe_allow_html=True)

if mg > daily_limit:
    st.markdown(f"""
    <div class="alert-card red-alert">
        <div class="alert-icon">🔴</div>
        <div>
            <div class="alert-title">Excessive Intake</div>
            <div class="alert-desc">You have exceeded your recommended caffeine limit of {daily_limit} mg/day. Current intake: {mg} mg.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    pct = mg / daily_limit * 100
    if pct > 75:
        st.markdown(f"""
        <div class="alert-card yellow-alert">
            <div class="alert-icon">🟡</div>
            <div>
                <div class="alert-title">Approaching Limit</div>
                <div class="alert-desc">You have consumed {mg} mg ({pct:.0f}%) of your {daily_limit} mg daily limit.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="alert-card green-alert">
            <div class="alert-icon">🟢</div>
            <div>
                <div class="alert-title">Safe Intake</div>
                <div class="alert-desc">Your caffeine intake of {mg} mg is within the recommended range of {daily_limit} mg/day.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

sleep_warning = False
try:
    from utils import compute_sleep_impact
    score, _, _ = compute_sleep_impact(mg, st.session_state.bedtime)
    sleep_warning = score != "GREEN"
except:
    pass

if sleep_warning:
    st.markdown(f"""
    <div class="alert-card yellow-alert">
        <div class="alert-icon">🟡</div>
        <div>
            <div class="alert-title">Sleep Risk</div>
            <div class="alert-desc">Today's caffeine schedule may affect sleep quality. Consider adjusting your intake timing.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if mg > 0:
    st.markdown(f"""
    <div class="alert-card green-alert">
        <div class="alert-icon">🟢</div>
        <div>
            <div class="alert-title">Caffeine Logged Successfully</div>
            <div class="alert-desc">Your {st.session_state.source_label} consumption of {mg} mg has been recorded.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    if st.button("📋 Final Report →", type="primary"):
        st.switch_page("pages/10_Final_Report.py")
with col2:
    if st.button("🏠 Back to Home"):
        st.switch_page("app.py")

st.markdown("""
<div style="text-align:center;padding:2rem;color:#999;font-size:0.85rem;margin-top:2rem;">
    © 2026 CaffiSense
</div>
""", unsafe_allow_html=True)
