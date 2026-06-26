import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
st.set_page_config(page_title="Analytics Dashboard - CaffiSense", page_icon="☕", layout="wide")
from utils import init_session_state, get_recommendations
init_session_state()

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.5rem; }
    .section-title { font-size: 1.3rem; font-weight: 600; color: #333; margin: 1.5rem 0 1rem; border-bottom: 2px solid #f0f0f0; padding-bottom: 0.5rem; }
    .chart-card { background: white; border-radius: 16px; padding: 1.5rem; border: 1px solid #f0f0f0; box-shadow: 0 2px 10px rgba(0,0,0,0.03); }
    .stButton > button { border-radius: 40px; font-weight: 600; padding: 0.5rem 2rem; width: 100%; }
</style>
""", unsafe_allow_html=True)

daily_limit, _ = get_recommendations(st.session_state.age, st.session_state.weight, st.session_state.sensitivity, st.session_state.health_conditions)
mg = st.session_state.predicted_caffeine

st.markdown('<div class="page-title">📊 Visual Analytics Dashboard</div>', unsafe_allow_html=True)
st.markdown('<p style="color:#666;">Visualize your caffeine intake patterns and trends.</p>', unsafe_allow_html=True)

g1, g2 = st.columns(2)

with g1:
    st.markdown('<div class="section-title">Daily Caffeine Intake</div>', unsafe_allow_html=True)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    values = [mg * (0.7 + i * 0.1) for i in range(7)]
    import random
    random.seed(42)
    values = [max(20, min(400, v + random.randint(-20, 20))) for v in values]
    fig = px.bar(x=days, y=values, labels={'x': 'Day', 'y': 'Caffeine (mg)'},
                 color_discrete_sequence=['#6b48ff'] * 7)
    fig.update_layout(
        plot_bgcolor='white', paper_bgcolor='white',
        margin=dict(l=20, r=20, t=20, b=20),
        yaxis_range=[0, max(values) * 1.2],
        height=300, showlegend=False
    )
    fig.update_traces(marker=dict(line=dict(width=0)), width=0.6)
    st.plotly_chart(fig, use_container_width=True)

with g2:
    st.markdown('<div class="section-title">Caffeine Source Distribution</div>', unsafe_allow_html=True)
    source = st.session_state.source_label or "Coffee"
    labels = [source]
    sizes = [mg]
    others = {"Coffee": 80, "Tea": 30}
    for s, v in others.items():
        if s != source:
            labels.append(s)
            sizes.append(v)
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=0.4,
                                 marker=dict(colors=['#6b48ff', '#a855f7', '#c084fc', '#d8b4fe']))])
    fig.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10),
                      paper_bgcolor='white', showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

g3, g4 = st.columns(2)

with g3:
    st.markdown('<div class="section-title">Intake vs Recommended Limit</div>', unsafe_allow_html=True)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=days, y=[daily_limit] * 7, mode='lines+markers',
        name='Recommended Limit', line=dict(color='#22c55e', width=3, dash='dash')
    ))
    fig.add_trace(go.Scatter(
        x=days, y=values, mode='lines+markers',
        name='Actual Intake', line=dict(color='#6b48ff', width=3)
    ))
    fig.update_layout(
        plot_bgcolor='white', paper_bgcolor='white',
        margin=dict(l=20, r=20, t=20, b=20),
        height=300, legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    st.plotly_chart(fig, use_container_width=True)

with g4:
    st.markdown('<div class="section-title">Sleep Impact Trend</div>', unsafe_allow_html=True)
    scores = [85, 72, 60, 55, 68, 75, 65]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=days, y=scores, mode='lines+markers',
        name='Sleep Score', line=dict(color='#eab308', width=3),
        fill='tozeroy', fillcolor='rgba(234,179,8,0.15)'
    ))
    fig.add_trace(go.Scatter(
        x=days, y=[70] * 7, mode='lines',
        name='Healthy Threshold', line=dict(color='#22c55e', width=2, dash='dash')
    ))
    fig.update_layout(
        plot_bgcolor='white', paper_bgcolor='white',
        margin=dict(l=20, r=20, t=20, b=20),
        yaxis_range=[0, 100], height=300,
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    if st.button("🔔 View Alerts & Notifications →", type="primary"):
        st.switch_page("pages/9_Alerts.py")
with col2:
    if st.button("📋 Final Report →"):
        st.switch_page("pages/10_Final_Report.py")

st.markdown("""
<div style="text-align:center;padding:2rem;color:#999;font-size:0.85rem;margin-top:2rem;">
    © 2026 CaffiSense
</div>
""", unsafe_allow_html=True)
