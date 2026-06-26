import streamlit as st
st.set_page_config(page_title="User Profile - CaffiSense", page_icon="☕", layout="wide")
from utils import init_session_state, HEALTH_WARNINGS
init_session_state()

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.5rem; }
    .section-title { font-size: 1.3rem; font-weight: 600; color: #333; margin: 1.5rem 0 1rem; border-bottom: 2px solid #f0f0f0; padding-bottom: 0.5rem; }
    .stButton > button { border-radius: 40px; font-weight: 600; padding: 0.5rem 2rem; width: 100%; }
    .example-tag { display: inline-block; background: #f3f0ff; color: #6b48ff; padding: 0.2rem 0.8rem; border-radius: 20px; font-size: 0.8rem; margin: 0.2rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">☕ User Profile</div>', unsafe_allow_html=True)
st.markdown('<p style="color:#666;">Set up your personal information for personalized recommendations.</p>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section-title">Personal Information</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.age = st.number_input("Age", min_value=10, max_value=120, value=st.session_state.age)
    with col2:
        st.session_state.weight = st.number_input("Weight (kg)", min_value=20, max_value=300, value=st.session_state.weight)

    st.markdown('<div class="section-title">Daily Schedule</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.session_state.wake_time = st.text_input("Wake-up Time", value=st.session_state.wake_time, help="HH:MM format")
    with col2:
        st.session_state.bedtime = st.text_input("Bedtime", value=st.session_state.bedtime, help="HH:MM format")
    with col3:
        st.session_state.workout_time = st.text_input("Workout Time", value=st.session_state.workout_time, help="HH:MM format")

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.work_start = st.text_input("Work/Study Start Time", value=st.session_state.work_start, help="HH:MM format")
    with col2:
        st.session_state.work_end = st.text_input("Work/Study End Time", value=st.session_state.work_end, help="HH:MM format")

    st.markdown('<div class="section-title">Caffeine Sensitivity</div>', unsafe_allow_html=True)
    st.session_state.sensitivity = st.radio(
        "How sensitive are you to caffeine?",
        options=["Low", "Medium", "High"],
        index=["Low", "Medium", "High"].index(st.session_state.sensitivity),
        horizontal=True,
    )

    st.markdown('<div class="section-title">Health Conditions</div>', unsafe_allow_html=True)
    st.session_state.has_health_issues = st.radio(
        "Do you have any health issues?",
        options=["No", "Yes"],
        index=0 if st.session_state.has_health_issues == "No" else 1,
        horizontal=True,
    )

    if st.session_state.has_health_issues == "Yes":
        st.markdown("##### Enter Health Condition(s)")
        health_opts = ["Hypertension", "Heart Disease", "Anxiety", "Insomnia", "Diabetes", "GERD", "Migraine", "Other"]
        selected = st.multiselect("Select health conditions", health_opts, default=st.session_state.health_conditions)
        st.session_state.health_conditions = selected
        st.markdown("Examples: " + " ".join([f'<span class="example-tag">{c}</span>' for c in health_opts]), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Next →", type="primary"):
        st.switch_page("pages/2_Caffeine_Source.py")

st.markdown("""
<div style="text-align:center;padding:2rem;color:#999;font-size:0.85rem;margin-top:2rem;">
    © 2026 CaffiSense
</div>
""", unsafe_allow_html=True)
