# COVID-19 Vaccine Adverse Event Risk Predictor
This project uses machine learning to predict the likelihood of serious adverse events following an mRNA COVID-19 vaccine. It's built on real-world data from the Vaccine Adverse Event Reporting System (VAERS).
You can try the live, interactive version of the model here:
(https://vaccine-risk-predictor-app.streamlit.app/Problem_Statement)
## The Goal
The main objective was to see if a machine learning model could identify individuals at a higher risk of a serious reaction based on initial data like the vaccine manufacturer and dose number. This project explores the application of data science in a public health context, focusing on creating a transparent and understandable tool.
## How It Works
The Data: The model was trained on an anonymized dataset of patient survey information related to vaccine side effects. A key challenge was the imbalanced nature of the data—serious events are far less common than mild ones.
The Model: A Random Forest Classifier was used for the prediction task. This model is effective at handling complex relationships in the data and is more robust to overfitting than a single decision tree. Special care was taken to handle the class imbalance by weighting the "Serious" cases more heavily during training.
## The App:
A simple web interface was built using Streamlit to make the model interactive. Users can input basic information, and the app provides a real-time risk assessment based on the model's prediction probability.
___ 
## Local Setup
If you want to run the app on your own machine:
Clone the repository:
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name


## Install the required libraries:
pip install -r requirements.txt


## Run the Streamlit app:
streamlit run app.py


Disclaimer: This is a student project for academic purposes and is not intended for medical advice. The model's predictions are based on statistical patterns and should not be used to make health decisions.
