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

# --- LOAD THE SAVED MODEL AND COLUMNS ---
try:
    model = joblib.load('vaccine_risk_model.joblib')
    # ** CHANGE 1: Load the list of model columns **
    model_columns = joblib.load('model_columns.joblib') 
except FileNotFoundError as e:
    st.error(f"A required file was not found: {e.filename}. Please ensure all model files are present.")
    st.stop()

# --- PREDICTION FUNCTION (MODIFIED) ---
def create_prediction_input(manu, dose, route, site, columns):
    # ** CHANGE 2: Use the loaded list of columns to build the input data **
    # This ensures all required columns are present, initialized to 0.
    input_data = {col: 0 for col in columns}

    # Set the numerical and categorical features based on user input
    input_data['VAX_DOSE_SERIES'] = dose

    # Use .get() to avoid errors if a column doesn't exist (though it should)
    if manu == 'MODERNA':
        input_data['VAX_MANU_MODERNA'] = 1
    elif manu == 'PFIZER\\BIONTECH':
        input_data['VAX_MANU_PFIZER\\BIONTECH'] = 1

    if route == 'Intramuscular (IM)':
        input_data['VAX_ROUTE_IM'] = 1
    elif route == 'Syringe (SYR)':
        input_data['VAX_ROUTE_SYR'] = 1
    
    # Add other routes if they are in your model columns
    # Example: if 'VAX_ROUTE_OT' is a feature
    elif route == 'Other':
        if 'VAX_ROUTE_OT' in input_data:
             input_data['VAX_ROUTE_OT'] = 1
             
    if site == 'Left Arm (LA)':
        input_data['VAX_SITE_LA'] = 1
    elif site == 'Right Arm (RA)':
        input_data['VAX_SITE_RA'] = 1

    # Convert the dictionary to a pandas DataFrame
    # ** CHANGE 3: Ensure the DataFrame columns are in the exact same order as the training data **
    return pd.DataFrame([input_data])[columns]


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
        ('PFIZER\\BIONTECH', 'MODERNA') # Only show main options in the GUI
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
    # ** CHANGE 4: Pass the model_columns list to the function **
    prediction_df = create_prediction_input(vax_manu, vax_dose, vax_route, vax_site, model_columns)

    # Get the prediction probability
    prediction_proba = model.predict_proba(prediction_df)[0][1]
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
        st.write("Input Features Sent to Model (all columns must match the training data):")
        st.dataframe(prediction_df)
