http://127.0.0.1:5000
# ☕ CaffiSense

> **AI-Based Personalized Caffeine Prediction, Health-Aware Recommendation, and Consumption Timing System**

CaffiSense is a smart caffeine management application that helps users understand, monitor, and optimize their daily caffeine consumption. It analyzes personal details, lifestyle, health conditions, workout schedule, and caffeine sources to provide personalized recommendations for safe and effective caffeine intake.

The application aims to improve productivity, support workout performance, reduce sleep disturbances, and encourage healthier caffeine consumption habits.

---

## 📖 Table of Contents

- About the Project
- Problem Statement
- Objectives
- Key Features
- Supported Caffeine Sources
- Project Workflow
- Technology Stack
- System Modules
- Future Scope
- Project Structure
- Installation
- Usage
- Screens
- Contributors
- License

---

# 📌 About the Project

Millions of people consume caffeine every day through coffee, tea, energy drinks, chocolates, soft drinks, and supplements. However, most people do not know:

- How much caffeine they consume daily.
- The best time to consume caffeine.
- Whether caffeine affects their sleep.
- How health conditions influence caffeine consumption.
- Whether they are exceeding safe caffeine limits.

CaffiSense solves these problems by providing intelligent and personalized caffeine recommendations based on scientific calculations and user information.

---

# ❓ Problem Statement

Many people consume caffeine without understanding its effects on their health, productivity, workouts, and sleep.

Existing caffeine trackers usually only record intake and provide general advice. They rarely consider personal factors such as:

- Age
- Weight
- Sleep schedule
- Workout timing
- Health conditions
- Caffeine sensitivity

CaffiSense combines all these factors into one intelligent recommendation system.

---

# 🎯 Objectives

The main objectives of CaffiSense are:

- Predict caffeine content from different caffeine sources.
- Recommend safe daily caffeine intake.
- Consider user health conditions.
- Suggest the best time to consume caffeine.
- Improve workout performance through caffeine timing.
- Estimate sleep impact.
- Promote healthy caffeine habits.
- Provide easy-to-understand recommendations.

---

# ✨ Key Features

### 👤 User Profile

Users enter:

- Age
- Weight
- Wake-up time
- Bedtime
- Work/Study schedule
- Workout time
- Caffeine sensitivity
- Health conditions (optional)

---

### ☕ Multiple Caffeine Sources

Supports:

- Coffee
- Tea
- Energy Drinks
- Soft Drinks
- Chocolates
- Cocoa Drinks
- Pre-Workout Drinks
- Caffeinated Sports Drinks
- Caffeine Tablets/Capsules

---

### 🤖 AI Caffeine Prediction

Predicts caffeine content based on:

- Beverage type
- Serving size
- Brew time
- Roast level
- Product details

---

### ❤️ Health-Aware Recommendations

Provides personalized guidance based on:

- Age
- Weight
- Health conditions
- Lifestyle
- Caffeine sensitivity

---

### 💪 Workout Optimization

Suggests:

- Best pre-workout caffeine timing
- Safe caffeine usage before exercise

---

### ⏰ Timing Optimization

Recommends:

- First caffeine intake
- Best productivity window
- Last safe caffeine consumption time

---

### 😴 Sleep Impact Prediction

Calculates:

- Estimated caffeine remaining before bedtime
- Sleep Impact Score
- Sleep warnings

---

### 📊 Dashboard

Displays:

- Daily intake
- Weekly trends
- Monthly reports
- Source distribution
- Sleep trends
- Recommended vs Actual intake

---

### 📄 Final Report

Generates a complete report including:

- User profile
- Caffeine analysis
- Recommendations
- Health warnings
- Sleep analysis

---

# ☕ Supported Caffeine Sources

- Coffee
- Tea
- Energy Drinks
- Soft Drinks
- Chocolates
- Cocoa Drinks
- Pre-Workout Drinks
- Caffeinated Sports Drinks
- Caffeine Tablets/Capsules

---

# 🔄 Project Workflow

```text
Home
   │
   ▼
User Profile
   │
   ▼
Health Assessment
   │
   ▼
Select Caffeine Source
   │
   ▼
Enter Beverage Details
   │
   ▼
AI Caffeine Prediction
   │
   ▼
Personalized Recommendations
   │
   ▼
Health Analysis
   │
   ▼
Timing Optimization
   │
   ▼
Sleep Impact Analysis
   │
   ▼
Analytics Dashboard
   │
   ▼
Final Report
```

---

# 🧩 System Modules

## 1. User Profile Module

Collects:

- Age
- Weight
- Wake-up time
- Bedtime
- Workout time
- Work schedule
- Health conditions
- Caffeine sensitivity

---

## 2. Caffeine Source Module

Allows users to select the caffeine source and enter product-specific information.

---

## 3. AI Prediction Module

Predicts caffeine content using machine learning.

---

## 4. Recommendation Engine

Analyzes:

- Personal profile
- Lifestyle
- Health conditions
- Predicted caffeine amount

Generates personalized recommendations.

---

## 5. Health Analysis Module

Provides recommendations for users with conditions like:

- Anxiety
- Hypertension
- Insomnia
- Diabetes
- GERD
- Heart disease
- Migraine

---

## 6. Workout Optimization Module

Suggests the best caffeine timing before exercise.

---

## 7. Sleep Analysis Module

Calculates:

- Remaining caffeine at bedtime
- Sleep Impact Score
- Sleep recommendations

---

## 8. Dashboard Module

Visualizes:

- Intake trends
- Sleep impact
- Caffeine source distribution
- Daily statistics

---

## 9. Report Generation Module

Creates downloadable reports in PDF format.

---

# 💻 Technology Stack

## Frontend

- React.js
- HTML5
- CSS3
- JavaScript

## Backend

- Python
- Flask / FastAPI

## Machine Learning

- Scikit-learn
- Pandas
- NumPy

## Database

- SQLite

## Visualization

- Chart.js / Recharts

---

# 📂 Suggested Project Structure

```
CaffiSense/
│
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── assets/
│   ├── styles/
│   └── App.js
│
├── backend/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── app.py
│   └── requirements.txt
│
├── dataset/
│
├── machine_learning/
│
├── reports/
│
├── README.md
│
└── LICENSE
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/CaffiSense.git
```

Move into the project directory

```bash
cd CaffiSense
```

Install frontend dependencies

```bash
npm install
```

Start the frontend

```bash
npm start
```

Install backend dependencies

```bash
pip install -r requirements.txt
```

Run the backend

```bash
python app.py
```

---

# ▶️ Usage

1. Open the application.
2. Create your profile.
3. Enter your daily schedule.
4. Add health conditions (if any).
5. Select a caffeine source.
6. Enter beverage details.
7. Predict caffeine content.
8. View personalized recommendations.
9. Check workout guidance.
10. Review sleep impact.
11. Download the final report.

---

# 📱 Main Screens

- 🏠 Home
- 👤 User Profile
- ❤️ Health Assessment
- ☕ Caffeine Source Selection
- 🤖 AI Prediction
- 📋 Recommendation Dashboard
- 💪 Workout Optimization
- 😴 Sleep Impact Analysis
- 📊 Analytics Dashboard
- 📄 Final Report

---

# 🌱 Future Scope

Future versions may include:

- Barcode scanner
- AI chatbot
- Smartwatch integration
- Voice assistant
- Wearable device support
- Multi-language support
- Cloud synchronization
- Personalized AI coaching

---

# 👨‍💻 Contributors

**Project Name:** CaffiSense

Developed as an academic/project work on AI-based personalized caffeine management.

---

# 📜 License

This project is intended for educational and research purposes.

You may modify and extend it for learning, research, and academic use.

---

# ⭐ Project Summary

CaffiSense is an AI-powered caffeine management system that predicts caffeine content from multiple sources and provides personalized recommendations based on a user's profile, health conditions, workout schedule, caffeine sensitivity, and daily routine. The application helps users make informed decisions about caffeine consumption, improve productivity, optimize workouts, reduce sleep disturbances, and build healthier lifestyle habits through intelligent analysis and easy-to-understand recommendations.
