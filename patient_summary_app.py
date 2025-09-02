import streamlit as st
import pandas as pd
patient_id=3

@st.cache_data
def load_summary_data():
    details_df = pd.read_csv("all_patients_details.csv")
    history_df = pd.read_csv("medical_history.csv")
    records_df = pd.read_csv("health_records.csv")
    return details_df, history_df, records_df

def show_patient_summary(patient_id):
    details_df, history_df, records_df = load_summary_data()

    info = details_df[details_df['patient_id'] == patient_id]
    history = history_df[history_df['patient_id'] == patient_id]
    records = records_df[records_df['patient_id'] == patient_id]

    if info.empty or history.empty or records.empty:
        st.error("❌ Patient data not found.")
        return

    data = pd.merge(info, history, on='patient_id')
    data = pd.merge(data, records, on='patient_id')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👤 Personal Info")
        st.markdown(f"**Name:** {data['name'].values[0]}")
        st.markdown(f"**Age:** {data['age'].values[0]}")
        st.markdown(f"**Gender:** {data['gender'].values[0]}")
        st.markdown(f"**Contact:** {data['contact_info'].values[0]}")
        st.markdown(f"**Address:** {data['address'].values[0]}")
        st.markdown(f"**Emergency Contact:** {data['emergency_contact'].values[0]}")

    with col2:
        st.subheader("📋 Health Snapshot")
        def flag(val, normal): return f"🔴 {val}" if val < normal[0] or val > normal[1] else f"🟢 {val}"
        st.markdown(f"**Systolic BP:** {flag(data['blood_pressure_systolic'].values[0], (90, 140))} mmHg")
        st.markdown(f"**Diastolic BP:** {flag(data['blood_pressure_diastolic'].values[0], (60, 90))} mmHg")
        st.markdown(f"**Heart Rate:** {flag(data['heart_rate'].values[0], (60, 100))} bpm")
        st.markdown(f"**Blood Sugar:** {flag(data['blood_sugar_level'].values[0], (70, 140))} mg/dL")
        st.markdown(f"**BMI:** {flag(data['BMI'].values[0], (18.5, 24.9))}")
        st.markdown(f"**Conditions:** {data['previous_medical_condition'].values[0]}")
        st.markdown(f"**Medications:** {data['medications_used'].values[0]}")

    st.subheader("📊 Risk Assessment")
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

    st.subheader("📈 Quick Visuals")
    st.line_chart(data[['blood_pressure_systolic', 'blood_pressure_diastolic']])
    st.bar_chart(data[['heart_rate', 'blood_sugar_level', 'BMI']])
if st.button("Summarise"):
    show_patient_summary(patient_id)
