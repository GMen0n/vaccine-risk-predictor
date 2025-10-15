import streamlit as st

st.set_page_config(
    page_title="Problem Statement",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Project: COVID-19 Vaccine Adverse Event Risk Prediction")
st.header("Predicting Event Severity Following Receipt of mRNA Based COVID-19 Vaccines, 2021")

st.divider()

st.subheader("Project Aim")
st.write(
    """
    This project aims to predict adverse events following the administration of mRNA-based 
    COVID-19 vaccines through supervised classification models. Utilizing anonymized 
    patient survey datasets, the goal is to develop risk models that predict the 
    likelihood of vaccine side effects using demographic, health, and prior reaction data as features.
    """
)

st.subheader("What is mRNA?")
st.write(
    """
    **mRNA** stands for **messenger RNA** — it’s a type of RNA (ribonucleic acid) that carries the genetic instructions from **DNA** to the **ribosomes**, where proteins are made.  
    """
)

st.subheader("Key Tasks & Methodology")
st.markdown(
    """
    - **Data Cleaning & Feature Engineering:** A significant task is to handle missing or imbalanced data entries, which is common in real-world datasets.
    
    - **Model Implementation:** Implement classifiers such as logistic regression, **random forests**, or **gradient boosting**, focusing on producing calibrated probability outputs to aid in risk assessment.
    
    - **Model Evaluation:** The model's clinical utility is evaluated using tools like **confusion matrices** and **precision-recall curves**.
    
    - **Ethical Considerations:** The project requires careful and ethical handling of sensitive health data.
    """
)

st.subheader("Desired Outcomes")
st.info(
    """
    The key outcome is to produce **transparent predictors with actionable interpretations** that can be valuable for public health frameworks. The model should not only be predictive 
    but also explainable.
    """,
    icon="🎯"
)

st.image(
    "https://raw.githubusercontent.com/GMen0n/vaccine-risk-predictor/refs/heads/main/assets/Confusion%20Matrix.png",
    caption="Placeholder for model evaluation charts like the Confusion Matrix or ROC Curve."
)
