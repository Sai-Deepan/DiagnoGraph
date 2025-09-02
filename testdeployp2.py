import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from st_circular_progress import CircularProgress  

st.set_page_config(page_title="Medical Report Dashboard", layout="wide")
st.title("Medical Report Dashboard")

with st.sidebar:
    st.title("Patient Details")
    patient_id = st.text_input("Enter Patient ID", value="P123456")
    patient_id = patient_id.strip()  


def load_summary_data():
    details_df = pd.read_csv("all_patients_details.csv")
    history_df = pd.read_csv("medical_history.csv")
    records_df = pd.read_csv("health_records.csv")


    for df in [details_df, history_df, records_df]:
        if 'patient_id' in df.columns:
            df['patient_id'] = df['patient_id'].astype(str).str.strip()

    return details_df, history_df, records_df


details_df, history_df, records_df = load_summary_data()
bp_data = records_df[records_df['patient_id'] == patient_id]


if 'date_recorded' in bp_data.columns:
    bp_data['date_recorded'] = pd.to_datetime(bp_data['date_recorded'], errors='coerce')
    bp_data = bp_data.sort_values('date_recorded')
    bp_data = bp_data.groupby('date_recorded').mean(numeric_only=True).reset_index()

st.header("Patient Details")


st.subheader("Blood Pressure")
if not bp_data.empty:
    bp_df = bp_data[['date_recorded', 'blood_pressure_systolic', 'blood_pressure_diastolic']].set_index('date_recorded')
    st.line_chart(bp_df.rename(columns={
        'blood_pressure_systolic': 'Systolic (mmHg)',
        'blood_pressure_diastolic': 'Diastolic (mmHg)'
    }))
else:
    st.warning("No blood pressure data available for this patient.")


st.subheader("Heart Rate")
if not bp_data.empty:
    hr_df = bp_data[['date_recorded', 'heart_rate']].set_index('date_recorded')
    st.area_chart(hr_df.rename(columns={'heart_rate': 'Heart Rate (bpm)'}))
else:
    st.warning("No heart rate data available for this patient.")


st.subheader("Respiratory Rate")
np.random.seed(42)
resp_rate = np.random.randint(12, 25, size=15)
resp_data = pd.DataFrame({
    "Respiratory Rate (breaths/min)": resp_rate
})
st.bar_chart(resp_data)


st.subheader("Blood Glucose")
if not bp_data.empty:
    glucose_df = bp_data[['date_recorded', 'blood_sugar_level']].set_index('date_recorded')
    st.line_chart(glucose_df.rename(columns={'blood_sugar_level': 'Blood Glucose (mg/dL)'}))
else:
    st.warning("No blood glucose data available for this patient.")

st.divider()


st.header("Vitals")
if not bp_data.empty:
    vitals_df = bp_data[['date_recorded', 'BMI']].set_index('date_recorded')
    st.line_chart(vitals_df.rename(columns={'BMI': 'BMI'}))
else:
    st.warning("No vitals data available for this patient.")

st.divider()

st.header("Alerts & Flags")

st.divider()


st.header("General")

with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Weight")
        bmi_value = 22.5
        max_bmi = 40.0
        progress_percent = int((bmi_value / max_bmi) * 100)
        progress_percent = min(100, max(0, progress_percent))

        cp1 = CircularProgress(
            label="Weight",
            value=progress_percent,
            key="weight_progress",
            size="large",
            color="rgb(255, 182, 193)",
            track_color="rgb(222, 235, 245)",
        )
        cp1.st_circular_progress()

        st.markdown(f"<h1 style='text-align: center;'>{bmi_value} </h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>BMI Value </p>", unsafe_allow_html=True)

    with col2:
        st.subheader("BMI")
        bmi_value = 22.5
        max_bmi = 40.0
        progress_percent = int((bmi_value / max_bmi) * 100)
        progress_percent = min(100, max(0, progress_percent))

        cp = CircularProgress(
            label="BMI",
            value=progress_percent,
            key="bmi_progress",
            size="large",
            color="rgb(255, 182, 193)",
            track_color="rgb(222, 235, 245)",
        )
        cp.st_circular_progress()

        st.markdown(f"<h1 style='text-align: center;'>{bmi_value} </h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>BMI Value </p>", unsafe_allow_html=True)

        if bmi_value < 18.5:
            st.info("UnderWeight")
        elif 18.5 <= bmi_value < 25.0:
            st.success("Healthy")
        elif 25.0 <= bmi_value < 30.0:
            st.warning("OverWeight")
        else:
            st.error("Obese")

def show_patient_summary(patient_id):
    details_df, history_df, records_df = load_summary_data()

    info = details_df[details_df['patient_id'] == patient_id]
    history = history_df[history_df['patient_id'] == patient_id]
    records = records_df[records_df['patient_id'] == patient_id]

    if info.empty or history.empty or records.empty:
        st.error("Patient data not found.")
        return

    data = pd.merge(info, history, on='patient_id')
    data = pd.merge(data, records, on='patient_id')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Personal Info")
        st.markdown(f"Name: {data['name'].values[0]}")
        st.markdown(f"Age: {data['age'].values[0]}")
        st.markdown(f"Gender: {data['gender'].values[0]}")
        st.markdown(f"Contact: {data['contact_info'].values[0]}")
        st.markdown(f"Address: {data['address'].values[0]}")
        st.markdown(f"Emergency Contact: {data['emergency_contact'].values[0]}")

    with col2:
        st.subheader("Health Report")
        def flag(val, normal): return f"🔴 {val}" if val < normal[0] or val > normal[1] else f"🟢 {val}"
        st.markdown(f"Systolic BP: {flag(data['blood_pressure_systolic'].values[0], (90, 140))} mmHg")
        st.markdown(f"Diastolic BP: {flag(data['blood_pressure_diastolic'].values[0], (60, 90))} mmHg")
        st.markdown(f"Heart Rate: {flag(data['heart_rate'].values[0], (60, 100))} bpm")
        st.markdown(f"Blood Sugar: {flag(data['blood_sugar_level'].values[0], (70, 140))} mg/dL")
        st.markdown(f"BMI: {flag(data['BMI'].values[0], (18.5, 24.9))}")
        st.markdown(f"Conditions: {data['previous_medical_condition'].values[0]}")
        st.markdown(f"Medications: {data['medications_used'].values[0]}")

    st.subheader("Risk Assessment")
    risk = 0
    if data['blood_pressure_systolic'].values[0] > 140: risk += 1
    if data['blood_sugar_level'].values[0] > 180: risk += 1
    if data['BMI'].values[0] > 30: risk += 1
    if risk == 0:
        st.success("🟢 Low Risk")
    elif risk == 1:
        st.warning("🟡 Moderate Risk")
    else:
        st.error("🔴 High Risk")



st.divider()


st.header("Medical History")

st.divider()


st.header("Current Medications")

st.divider()

review = st.text_area("Doctor's Review")
if st.button("Submit Review"):
    st.success("Review submitted successfully!")


st.divider()
st.header("Patient Summary")

if st.button("Summarise"):
    show_patient_summary(patient_id)
