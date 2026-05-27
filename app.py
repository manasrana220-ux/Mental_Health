# ==========================================
# MODERN AI MENTAL HEALTH PREDICTION SYSTEM
# FULL STREAMLIT APP
# ==========================================

import streamlit as st
import pandas as pd
import joblib
import requests
import time

from streamlit_lottie import st_lottie

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Mental Health AI",
    page_icon="🧠",
    layout="wide"
)

# ==========================================
# LOAD MODEL & SCALER
# ==========================================

model = joblib.load("mental_health_risk_model.pkl")
scaler = joblib.load("mental_health_risk_scaler.pkl")

# ==========================================
# LOAD LOTTIE ANIMATION
# ==========================================

def load_lottie(url):

    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()

lottie_mental = load_lottie(
    "https://assets9.lottiefiles.com/packages/lf20_xRmNN8.json"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {

    background: linear-gradient(
        -45deg,
        #0f172a,
        #1e293b,
        #0f172a,
        #1d4ed8
    );

    background-size: 400% 400%;
    animation: gradient 12s ease infinite;

    color: white;
}

@keyframes gradient {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

.card {

    background: rgba(255,255,255,0.08);

    backdrop-filter: blur(14px);

    border: 1px solid rgba(255,255,255,0.15);

    padding: 25px;

    border-radius: 25px;

    box-shadow: 0 8px 32px rgba(0,0,0,0.35);

    margin-bottom: 20px;

    transition: 0.4s;
}

.card:hover {

    transform: translateY(-5px);

    box-shadow: 0 10px 40px rgba(0,0,0,0.45);
}

h1, h2, h3, h4, h5, h6 {

    color: white;
}

.stButton>button {

    width: 100%;
    height: 60px;

    border: none;
    border-radius: 15px;

    background: linear-gradient(
        90deg,
        #06b6d4,
        #3b82f6
    );

    color: white;

    font-size: 20px;
    font-weight: bold;

    transition: 0.4s;
}

.stButton>button:hover {

    transform: scale(1.03);

    background: linear-gradient(
        90deg,
        #3b82f6,
        #06b6d4
    );

    box-shadow: 0 0 20px #3b82f6;
}

.result-box {

    padding: 35px;

    border-radius: 25px;

    text-align: center;

    font-size: 38px;
    font-weight: bold;

    color: white;

    animation: pulse 2s infinite;
}

.low {

    background: linear-gradient(
        90deg,
        #16a34a,
        #22c55e
    );
}

.medium {

    background: linear-gradient(
        90deg,
        #f59e0b,
        #facc15
    );
}

.high {

    background: linear-gradient(
        90deg,
        #dc2626,
        #ef4444
    );
}

@keyframes pulse {

    0% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.04);
    }

    100% {
        transform: scale(1);
    }
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2966/2966486.png",
        width=120
    )

    st.title("🧠 Mental Health AI")

    st.markdown("---")

    st.info(
        "AI powered system to predict mental health risk."
    )

   

# ==========================================
# TITLE
# ==========================================

st.markdown("""
<h1 style='text-align:center; font-size:55px;'>
🧠 Mental Health Risk Prediction
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center; color:lightgray;'>
AI Powered Mental Wellness Analysis
</h4>
""", unsafe_allow_html=True)

# ==========================================
# LOTTIE ANIMATION
# ==========================================

st_lottie(
    lottie_mental,
    height=300,
    key="mental"
)

# ==========================================
# TABS
# ==========================================

tab1, tab2 = st.tabs([
    "📝 Prediction Form",
    "ℹ️ About Project"
])

# ==========================================
# ABOUT TAB
# ==========================================

with tab2:

    st.markdown("""
    ## About This Project

    This system uses Machine Learning
    to predict mental health risk levels.

    ### Technologies Used

    - Streamlit
    - Scikit-learn
    - Pandas
    - Machine Learning
    - Python

    ### Prediction Categories

    - Low Risk
    - Medium Risk
    - High Risk
    """)

# ==========================================
# MAPPINGS
# ==========================================

risk_mapping = {
    0: 'Low Risk',
    1: 'Medium Risk',
    2: 'High Risk'
}

gender_map = {
    'Male': 0,
    'Female': 1,
    'Other': 2
}

marital_map = {
    'Single': 0,
    'Married': 1,
    'Divorced': 2
}

education_map = {
    'School': 0,
    'College': 1,
    'Graduate': 2,
    'Postgraduate': 3
}

employment_map = {
    'Student': 0,
    'Employed': 1,
    'Unemployed': 2
}

yes_no_map = {
    'Yes': 1,
    'No': 0
}

# ==========================================
# FORM TAB
# ==========================================

with tab1:

    with st.form("prediction_form"):

        # ==================================
        # BASIC DETAILS
        # ==================================

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("👤 Basic Information")

        col1, col2 = st.columns(2)

        with col1:

            age = st.number_input(
                "Age",
                10,
                100,
                22
            )

            gender = st.selectbox(
                "Gender",
                ["Male", "Female", "Other"]
            )

            marital_status = st.selectbox(
                "Marital Status",
                ["Single", "Married", "Divorced"]
            )

        with col2:

            education_level = st.selectbox(
                "Education Level",
                ["School", "College", "Graduate", "Postgraduate"]
            )

            employment_status = st.selectbox(
                "Employment Status",
                ["Student", "Employed", "Unemployed"]
            )

        st.markdown("</div>", unsafe_allow_html=True)

        # ==================================
        # HEALTH DETAILS
        # ==================================

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("💪 Lifestyle & Mental Health")

        col1, col2 = st.columns(2)

        with col1:

            sleep_hours = st.slider(
                "Sleep Hours",
                0.0, 12.0, 7.0
            )

            physical_activity = st.slider(
                "Physical Activity Hours / Week",
                0.0, 30.0, 5.0
            )

            screen_time = st.slider(
                "Screen Time Hours / Day",
                0.0, 20.0, 5.0
            )

            social_support = st.slider(
                "Social Support",
                1, 10, 5
            )

            financial_stress = st.slider(
                "Financial Stress",
                1, 10, 5
            )

        with col2:

            anxiety_score = st.slider(
                "Anxiety Level",
                1, 10, 5
            )

            depression_score = st.slider(
                "Depression Level",
                1, 10, 5
            )

            stress_level = st.slider(
                "Stress Level",
                1, 10, 5
            )

            mood_swings = st.slider(
                "Mood Swings",
                1, 10, 5
            )

            concentration_difficulty = st.slider(
                "Concentration Difficulty",
                1, 10, 5
            )

        st.markdown("</div>", unsafe_allow_html=True)

        # ==================================
        # CONDITIONAL QUESTIONS
        # ==================================

        academic_pressure = 0
        work_stress = 0
        job_satisfaction = 0
        working_hours = 0

        if employment_status == "Student":

            st.markdown("<div class='card'>", unsafe_allow_html=True)

            st.subheader("📚 Academic Information")

            academic_pressure = st.slider(
                "Academic Pressure",
                1, 10, 5
            )

            st.markdown("</div>", unsafe_allow_html=True)

        if employment_status == "Employed":

            st.markdown("<div class='card'>", unsafe_allow_html=True)

            st.subheader("💼 Work Information")

            work_stress = st.slider(
                "Work Stress",
                1, 10, 5
            )

            job_satisfaction = st.slider(
                "Job Satisfaction",
                1, 10, 5
            )

            working_hours = st.slider(
                "Working Hours / Week",
                1, 100, 40
            )

            st.markdown("</div>", unsafe_allow_html=True)

        # ==================================
        # HISTORY
        # ==================================

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("🩺 Mental Health History")

        col1, col2 = st.columns(2)

        with col1:

            panic_attack = st.selectbox(
                "Panic Attack History",
                ["Yes", "No"]
            )

            family_history = st.selectbox(
                "Family History",
                ["Yes", "No"]
            )

            previous_diagnosis = st.selectbox(
                "Previous Diagnosis",
                ["Yes", "No"]
            )

        with col2:

            therapy_history = st.selectbox(
                "Therapy History",
                ["Yes", "No"]
            )

            substance_use = st.selectbox(
                "Substance Use",
                ["Yes", "No"]
            )

        st.markdown("</div>", unsafe_allow_html=True)

        # ==================================
        # BUTTON
        # ==================================

        submit = st.form_submit_button(
            "🔍 Predict Mental Health Risk"
        )

# ==========================================
# PREDICTION
# ==========================================

if submit:

    input_data = {

        'age': age,
        'gender': gender_map[gender],
        'marital_status': marital_map[marital_status],
        'education_level': education_map[education_level],
        'employment_status': employment_map[employment_status],

        'sleep_hours': sleep_hours,

        'physical_activity_hours_per_week':
        physical_activity,

        'screen_time_hours_per_day':
        screen_time,

        'social_support_score':
        social_support,

        'work_stress_level':
        work_stress,

        'academic_pressure_level':
        academic_pressure,

        'job_satisfaction_score':
        job_satisfaction,

        'financial_stress_level':
        financial_stress,

        'working_hours_per_week':
        working_hours,

        'anxiety_score':
        anxiety_score,

        'depression_score':
        depression_score,

        'stress_level':
        stress_level,

        'mood_swings_frequency':
        mood_swings,

        'concentration_difficulty_level':
        concentration_difficulty,

        'panic_attack_history':
        yes_no_map[panic_attack],

        'family_history_mental_illness':
        yes_no_map[family_history],

        'previous_mental_health_diagnosis':
        yes_no_map[previous_diagnosis],

        'therapy_history':
        yes_no_map[therapy_history],

        'substance_use':
        yes_no_map[substance_use]
    }

    sample_input = pd.DataFrame([input_data])

    scaled_input = scaler.transform(sample_input)

    # ======================================
    # LOADING ANIMATION
    # ======================================

    with st.spinner(
        "🧠 AI is analyzing mental health patterns..."
    ):

        progress = st.progress(0)

        for i in range(100):

            time.sleep(0.01)

            progress.progress(i + 1)

        prediction = model.predict(scaled_input)

    # ======================================
    # RESULT
    # ======================================

    result = risk_mapping[prediction[0]]

    st.balloons()

    st.markdown("<br>", unsafe_allow_html=True)

    if result == "Low Risk":

        st.markdown(
            f"""
            <div class='result-box low'>
            ✅ {result}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(30)

    elif result == "Medium Risk":

        st.markdown(
            f"""
            <div class='result-box medium'>
            ⚠️ {result}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(65)

    else:

        st.markdown(
            f"""
            <div class='result-box high'>
            🚨 {result}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(95)

    st.success(
        "Prediction Completed Successfully!"
    )

    st.info(
        "This prediction is for educational "
        "purposes only and should not replace "
        "professional medical advice."
    )