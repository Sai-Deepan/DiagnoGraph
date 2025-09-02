# Sai

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from st_circular_progress import CircularProgress

st.set_page_config(page_title="Medical Report Dashboard", layout="wide")
st.title("Medical Report Dashboard")

st.header("Patient Details")

st.subheader("Blood Pressure")
np.random.seed(42)  # for reproducibility
systolic = np.random.randint(110, 160, size=20)    # typical systolic range
diastolic = np.random.randint(70, 100, size=20)    # typical diastolic range

bp_df = pd.DataFrame({
    "Systolic (mmHg)": systolic,
    "Diastolic (mmHg)": diastolic
})

st.line_chart(bp_df)

st.subheader("Heart Rate")
np.random.seed(42)
time_points = pd.date_range("2025-01-01", periods=30, freq="D")
heart_rate = np.random.randint(60, 110, size=30)  # realistic HR values

df = pd.DataFrame({
    "Heart Rate (bpm)": heart_rate
})

st.area_chart(df)

st.subheader("Respiratory Rate")

np.random.seed(42)
resp_rate = np.random.randint(12, 25, size=15)  # realistic range: 12–25 breaths/min

resp_data = pd.DataFrame({
    "Respiratory Rate (breaths/min)": resp_rate
})

st.bar_chart(resp_data)

st.subheader("Blood Glucose")

chart_date = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Fasting Blood Glucose', 'Postprandial', 'Random Blood Glucose']
)

st.line_chart(chart_date)

st.divider()

st.header("Vitals")

chart_5 = pd.DataFrame(
    np.random.randn(20, 1),
    columns=['Average Performance']
)
st.line_chart(chart_5)

st.divider()

st.header("Alerts & Flags")

st.divider()

st.header("General")

st.subheader("BMI")
bmi_value = 22.5
max_bmi = 40.0
progress_percent = int((bmi_value / max_bmi) * 100)
progress_percent = min(100, max(0, progress_percent))

with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        cp = CircularProgress(
            label="BMI",
            value=progress_percent,
            key="bmi_progress",
            size="large",
            color="rgb(255, 182, 193)",
            track_color="rgb(222, 235, 245)",
        )
        cp.st_circular_progress()

        st.markdown(f"<h1 style='text-align: center;'>{bmi_value}</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>BMI Value</p>", unsafe_allow_html=True)

if bmi_value < 18.5:
    st.info("UnderWeight")
elif 18.5 <= bmi_value < 25.0:
    st.success("Healthy")
elif 25.0 <= bmi_value < 30.0:
    st.warning("OverWeight")
else:
    st.error("Obese")

st.subheader("Weight")

st.divider()

st.header("Medical History")
df = pd.DataFrame({
    "Patient Details": ["John Doe, 54, Male, P123456"],
    "Chief Complaints": [", ".join(["Chest pain", "Shortness of breath", "Fatigue"])],
    "Allergies": [", ".join(["Penicillin"])],
    "Vitals (Latest)": [", ".join(["BP: 150/95 mmHg", "HR: 92 bpm", "RR: 20/min", "Temp: 98.6°F", "SpO2: 95%"])]
})

st.table(df)

st.divider()

st.header("Current Medications")
df = pd.DataFrame({
    "Past Medical History": [", ".join(["Hypertension (10 yrs)", "Type 2 Diabetes (5 yrs)"])],
    "Medications": [", ".join(["Metformin 500mg BID", "Amlodipine 5mg OD", "Atorvastatin 20mg HS"])],
    "Diagnosis": [", ".join(["Unstable angina", "Hypertension", "Type 2 Diabetes"])]

})
st.table(df)

st.divider()

with st.sidebar:
    st.title("Patient Details")
    st.text_input("Name")
    st.text_input("Age")
    st.text_input("Gender")
    st.text_area("Medical History")
    st.header("Current Medications")
    st.text_area("List medications here")

review = st.text_area("Doctor's Review")
if st.button("Submit Review"):
    st.success("Review submitted successfully!")
