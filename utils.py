import streamlit as st

def init_session_state():
    defaults = {
        'age': 22,
        'weight': 70,
        'wake_time': '07:00',
        'bedtime': '23:00',
        'work_start': '09:00',
        'work_end': '17:00',
        'workout_time': '18:00',
        'sensitivity': 'Medium',
        'has_health_issues': 'No',
        'health_conditions': [],
        'caffeine_source': None,
        'coffee_roast': 'Medium',
        'brew_time': 4,
        'serving_size': 250,
        'tea_type': 'Black Tea',
        'brew_duration': 3,
        'brand_name': '',
        'chocolate_type': 'Dark',
        'chocolate_weight': 50,
        'tablet_dose': 100,
        'tablet_qty': 1,
        'predicted_caffeine': 0,
        'source_label': '',
        'all_logs': [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def predict_caffeine(source, details):
    base = {
        'Coffee': (80, 200),
        'Tea': (15, 50),
        'Energy Drinks': (80, 150),
        'Soft Drinks': (30, 55),
        'Chocolates': (5, 20),
        'Cocoa Drinks': (5, 15),
        'Pre-Workout Drinks': (100, 300),
        'Caffeinated Sports Drinks': (50, 100),
        'Caffeine Tablets/Capsules': (50, 200),
    }
    low, high = base.get(source, (0, 100))
    import random
    return random.randint(low, high)

def get_recommendations(age, weight, sensitivity, conditions):
    base_limit = 400
    if sensitivity == 'Low':
        base_limit = 500
    elif sensitivity == 'Medium':
        base_limit = 300
    else:
        base_limit = 200
    if any(c in ['Hypertension', 'Heart Disease'] for c in conditions):
        base_limit = min(base_limit, 200)
    if 'Anxiety' in conditions:
        base_limit = min(base_limit, 250)
    if 'Insomnia' in conditions:
        base_limit = min(base_limit, 200)
    recs = []
    if 'Anxiety' in conditions:
        recs.append("Based on your anxiety condition, moderate caffeine consumption is recommended.")
        recs.append("Avoid consuming large doses in a single sitting.")
        recs.append("Prefer smaller doses distributed throughout the day.")
    if 'Hypertension' in conditions:
        recs.append("Monitor caffeine intake carefully due to hypertension.")
    if 'Insomnia' in conditions:
        recs.append("Avoid caffeine late in the evening to prevent sleep disruption.")
    if not recs:
        recs.append("Your caffeine intake is within safe limits. Maintain your current habits.")
        recs.append("Stay hydrated and avoid caffeine after 4 PM for better sleep.")
    return base_limit, recs

def compute_timing(wake_time, bedtime, workout_time):
    w_h, w_m = map(int, wake_time.split(':'))
    b_h, b_m = map(int, bedtime.split(':'))
    wo_h, wo_m = map(int, workout_time.split(':'))
    first_caffeine = f"{w_h + 1}:{w_m:02d}" if w_h + 1 < 12 else f"{w_h + 1}:{w_m:02d}"
    prod_start = f"{w_h + 2}:{w_m:02d}"
    prod_end = f"{w_h + 4}:{w_m:02d}"
    pre_workout = f"{wo_h - 1}:{wo_m:02d}"
    last_safe = f"{b_h - 3}:{b_m:02d}"
    if int(last_safe.split(':')[0]) < 12:
        last_safe = f"{int(last_safe.split(':')[0]) + 12}:{last_safe.split(':')[1]}"
    return first_caffeine, prod_start, prod_end, pre_workout, last_safe

def compute_sleep_impact(caffeine_mg, bedtime, now_hour=20):
    half_life = 5
    hours_until_bed = max(1, now_hour - int(bedtime.split(':')[0]))
    remaining = caffeine_mg * (0.5 ** (hours_until_bed / half_life))
    if remaining > 100:
        score = "RED"
    elif remaining > 50:
        score = "YELLOW"
    else:
        score = "GREEN"
    return score, round(remaining, 1), hours_until_bed

RISK_LEVELS = {
    'Low Risk': (0, 100),
    'Moderate Risk': (100, 250),
    'High Risk': (250, 999),
}

HEALTH_WARNINGS = {
    'Anxiety': 'High caffeine intake may increase nervousness and restlessness.',
    'Insomnia': 'Avoid caffeine late in the evening.',
    'Hypertension': 'Monitor caffeine intake carefully.',
    'Heart Disease': 'Consult your doctor before consuming caffeine.',
    'Diabetes': 'Monitor blood sugar levels when consuming caffeine.',
    'GERD': 'Caffeine may worsen acid reflux symptoms.',
    'Migraine': 'Caffeine can trigger or relieve migraines.',
}
