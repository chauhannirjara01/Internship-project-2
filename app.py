import streamlit as st
st.set_page_config(page_title="CaffiSense", page_icon="☕", layout="wide")
from utils import init_session_state
init_session_state()

st.markdown("""
<style>
    .hero-title { font-size: 3rem; font-weight: 800; color: #1a1a2e; line-height: 1.2; }
    .hero-sub { font-size: 1.2rem; color: #555; max-width: 600px; }
    .feature-card {
        background: #fff; border-radius: 16px; padding: 1.8rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #f0f0f0;
        transition: transform 0.2s; text-align: center; height: 100%;
    }
    .feature-card:hover { transform: translateY(-4px); }
    .feature-icon { font-size: 2.5rem; margin-bottom: 1rem; }
    .feature-title { font-size: 1.15rem; font-weight: 700; margin-bottom: 0.5rem; color: #1a1a2e; }
    .feature-desc { font-size: 0.9rem; color: #666; }
    .btn-primary {
        background: linear-gradient(135deg, #6b48ff, #a855f7);
        color: white; padding: 0.75rem 2rem; border-radius: 40px;
        font-weight: 600; border: none; cursor: pointer; text-decoration: none;
        display: inline-block; transition: opacity 0.2s;
    }
    .btn-primary:hover { opacity: 0.9; color: white; }
    .btn-secondary {
        background: transparent; color: #6b48ff; padding: 0.75rem 2rem;
        border-radius: 40px; font-weight: 600; border: 2px solid #6b48ff;
        cursor: pointer; text-decoration: none; display: inline-block;
        margin-left: 1rem; transition: all 0.2s;
    }
    .btn-secondary:hover { background: #6b48ff; color: white; }
    .nav-link { color: #444; text-decoration: none; font-weight: 500; margin: 0 1rem; }
    .nav-link:hover { color: #6b48ff; }
    .header { display: flex; align-items: center; justify-content: space-between; padding: 1rem 0; flex-wrap: wrap; gap: 1rem; }
    .logo { font-size: 1.5rem; font-weight: 800; color: #1a1a2e; }
    .stButton > button { border-radius: 40px; font-weight: 600; padding: 0.5rem 2rem; }
    .css-1kyxreq { display: flex; justify-content: center; }
    div[data-testid="stHorizontalBlock"] { gap: 1rem; }
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<div class="logo">☕ CaffiSense</div>', unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
        <a class="btn-primary" href="/" target="_self">Home</a>
    </div>
    """, unsafe_allow_html=True)

nav_cols = st.columns(6)
nav_items = ["Home", "About", "Features", "Start Analysis", "Contact"]
for i, item in enumerate(nav_items):
    with nav_cols[i]:
        if item == "Start Analysis":
            if st.button("Start Analysis", type="primary"):
                st.switch_page("pages/1_User_Profile.py")
        elif item == "Features":
            st.markdown(f'<a class="nav-link" href="#features">Features</a>', unsafe_allow_html=True)
        else:
            st.markdown(f'<span class="nav-link">{item}</span>', unsafe_allow_html=True)

st.markdown("<hr style='margin:0.5rem 0 2rem 0; opacity:0.1;'>", unsafe_allow_html=True)

hero_col1, hero_col2 = st.columns([3, 2])
with hero_col1:
    st.markdown('<div class="hero-title">Smart Caffeine Prediction &<br>Personalized Health Recommendations</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Analyze your caffeine intake, optimize productivity, improve workouts, and protect your sleep.</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    b1, b2 = st.columns([1, 1])
    with b1:
        if st.button("🚀 Start Analysis", use_container_width=True):
            st.switch_page("pages/1_User_Profile.py")
    with b2:
        st.markdown('<a class="btn-secondary" href="#features" style="text-align:center;">Learn More</a>', unsafe_allow_html=True)
with hero_col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 20px; padding: 3rem; text-align:center; color:white;">
        <div style="font-size:4rem;">☕</div>
        <div style="font-size:1.5rem;font-weight:700;">AI-Powered Analysis</div>
        <div style="opacity:0.8;">Get personalized recommendations</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<h2 id="features" style="text-align:center;font-size:2rem;font-weight:700;color:#1a1a2e;">Key Features</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;color:#666;margin-bottom:2rem;">Everything you need to manage your caffeine intake intelligently</p>', unsafe_allow_html=True)

features = [
    ("🤖", "AI Caffeine Prediction", "Predict caffeine content from various sources with machine learning accuracy."),
    ("❤️", "Health-Aware Recommendations", "Personalized suggestions based on your health conditions and profile."),
    ("💪", "Workout Optimization", "Get ideal pre-workout caffeine timing for maximum performance gains."),
    ("😴", "Sleep Impact Forecast", "Know how your caffeine consumption affects sleep quality."),
]
for i in range(0, 4, 2):
    cols = st.columns(2)
    for j, (icon, title, desc) in enumerate(features[i:i+2]):
        with cols[j]:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <div class="feature-title">{title}</div>
                <div class="feature-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;padding:2rem;background:linear-gradient(135deg,#667eea,#764ba2);border-radius:20px;color:white;">
    <div style="font-size:1.8rem;font-weight:700;margin-bottom:1rem;">Ready to Take Control of Your Caffeine Intake?</div>
    <p style="opacity:0.9;margin-bottom:1.5rem;">Start your personalized caffeine analysis journey today.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding:1rem 0; color:#999; font-size:0.85rem;">
    © 2026 CaffiSense — Smart Caffeine Prediction & Personalized Health Recommendations
</div>
""", unsafe_allow_html=True)
