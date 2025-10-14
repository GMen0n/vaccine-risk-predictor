import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Vaccine Adverse Event Predictor",
    page_icon="💉",
    layout="centered"
)

# --- LOAD THE SAVED MODEL ---
# Ensure the model file 'vaccine_risk_model.joblib' is in the same directory
try:
    model = joblib.load('vaccine_risk_model.joblib')
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'vaccine_risk_model.joblib' is present.")
    st.stop()

# --- PREDICTION FUNCTION ---
# This function creates the feature set that your model expects
def create_prediction_input(manu, dose, route, site):
    # These are the columns your model was trained on after one-hot encoding.
    # It's crucial that they match exactly!
    feature_columns = [
        'VAX_DOSE_SERIES', 'VAX_MANU_MODERNA', 'VAX_MANU_PFIZER\\BIONTECH',
        'VAX_ROUTE_IM', 'VAX_ROUTE_SYR', 'VAX_SITE_LA', 'VAX_SITE_RA'
    ] # Add any other columns your final model used!

    # Create a dictionary to hold the feature values
    input_data = {col: 0 for col in feature_columns}

    # Set the numerical and categorical features based on user input
    input_data['VAX_DOSE_SERIES'] = dose

    if manu == 'MODERNA':
        input_data['VAX_MANU_MODERNA'] = 1
    elif manu == 'PFIZER\\BIONTECH':
        input_data['VAX_MANU_PFIZER\\BIONTECH'] = 1

    if route == 'Intramuscular (IM)':
        input_data['VAX_ROUTE_IM'] = 1
    elif route == 'Syringe (SYR)':
        input_data['VAX_ROUTE_SYR'] = 1

    if site == 'Left Arm (LA)':
        input_data['VAX_SITE_LA'] = 1
    elif site == 'Right Arm (RA)':
        input_data['VAX_SITE_RA'] = 1

    # Convert the dictionary to a pandas DataFrame
    return pd.DataFrame([input_data])


# --- APP LAYOUT ---
st.title('💉 COVID-19 Vaccine Adverse Event Risk Predictor')
st.write(
    "This app predicts the probability of a serious adverse event following an mRNA COVID-19 vaccine. "
    "Select the patient's details below to get a risk assessment."
)

st.divider()

# --- USER INPUT WIDGETS ---
col1, col2 = st.columns(2)

with col1:
    vax_manu = st.selectbox(
        'Vaccine Manufacturer',
        ('PFIZER\\BIONTECH', 'MODERNA')
    )
    vax_route = st.selectbox(
        'Administration Route',
        ('Intramuscular (IM)', 'Syringe (SYR)', 'Other')
    )

with col2:
    vax_dose = st.selectbox('Dose Number', (1, 2, 3))
    vax_site = st.selectbox(
        'Administration Site',
        ('Left Arm (LA)', 'Right Arm (RA)', 'Other')
    )

# --- PREDICTION AND DISPLAY ---
if st.button('Predict Risk', type="primary"):
    # Create the input dataframe
    prediction_df = create_prediction_input(vax_manu, vax_dose, vax_route, vax_site)

    # Get the prediction probability
    prediction_proba = model.predict_proba(prediction_df)[0][1] # Probability of class '1' (Serious)
    risk_percentage = prediction_proba * 100

    st.subheader('Prediction Result')

    if risk_percentage > 50:
        st.warning(f"**High Risk** of a serious adverse event detected.")
    else:
        st.success(f"**Low Risk** of a serious adverse event detected.")

    st.metric(label="Predicted Probability of Serious Event", value=f"{risk_percentage:.2f}%")
    st.progress(int(risk_percentage))

    with st.expander("Show Advanced Details"):
        st.write("The prediction is based on a Random Forest model trained on VAERS data.")
        st.write("Input Features Sent to Model:")
        st.dataframe(prediction_df)