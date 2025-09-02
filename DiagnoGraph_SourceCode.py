import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from st_circular_progress import CircularProgress

st.set_page_config(page_title="Medical Report Dashboard", layout="wide")
st.title("Medical Report Dashboard")

st.header("Patient Details")
st.subheader("Blood Pressure")
chart_date = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'],
)

st.subheader("Heart Rate")
st.area_chart(chart_date)

st.subheader("Respiratory Rate")
st.bar_chart(chart_date)

st.subheader("Blood Glucose")
st.line_chart(chart_date)

st.divider()

st.header("Vitals")
scatter_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
})
st.scatter_chart(scatter_data)

st.divider()

st.header("Alerts & Flags")

st.divider()

st.header("General")
st.subheader("BMI")
st.subheader("Weight")

st.divider()

st.header("Medical History")

st.divider()

st.header("Current Medications")

st.divider()

with st.sidebar:
    st.title("Patient Details")
    st.text_input("Name")
    st.text_input("Age")
    st.text_input("Gender")
    st.text_area("Medical History")
    st.header("Current Medications")
    st.text_area("List medications here")

bmi_value = 22.5
max_bmi = 40.0
progress_percent = int((bmi_value / max_bmi) * 100)
progress_percent = min(100, max(0, progress_percent)) # Clamps the value between 0 and 100

with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        cp = CircularProgress(
            label="BMI",
            value=progress_percent,
            key="bmi_progress",
            size="large",
            color="rgb(32, 156, 255)",
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


review = st.text_area("Doctor's Review")
if st.button("Submit Review"):
    st.success("Review submitted successfully!")
