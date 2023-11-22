### App to use the model saved in a pkl file to make a prediction

### import libraries
import pandas as pd
import streamlit as st
import pickle



#######################################################################################################################################
### To launch the app on your local machine, follow these steps:
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open your terminal and navigate (cd) to the folder containing the *.py file
### 3. Execute... streamlit run app.py
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file
#######################################################################################################################################


# Title of the app
st.title("Disease early monitoring system")

## Subtitle
st.write("### Diabetes predictor")

### To position text and color, you can use html syntax
st.markdown("<h1 style='text-align: center; color: blue;'>Patient: </h1>", unsafe_allow_html=True)

# Load the model using pickle
pickled_pipe = pickle.load(open('../model/log-reg-best-model.pkl', 'rb'))


def main():
    st.title("Health Indicators Form")

    # Binary questions with selectbox for Yes/No
    has_high_bp = st.selectbox("Has the patient been told by a medical professional that they have high blood pressure?", ["Yes", "No"], key='has_high_bp')
    has_high_cholesterol = st.selectbox("Has the patient been told by a medical professional that they have high cholesterol?", ["Yes", "No"], key='has_high_cholesterol')
    checked_cholesterol = st.selectbox("Has the patient's cholesterol been checked in the last 5 years?", ["Yes", "No"], key='checked_cholesterol')
    is_smoker = st.selectbox("Has the patient smoked at least 100 cigarettes in their entire life?", ["Yes", "No"], key='is_smoker')
    had_stroke = st.selectbox("Has the patient ever had a stroke?", ["Yes", "No"], key='had_stroke')
    has_heart_disease = st.selectbox("Does the patient have Coronary Heart Disease or myocardial infarction?", ["Yes", "No"], key='has_heart_disease')
    physical_activity = st.selectbox("Did the patient do any physical activity in the past 30 days?", ["Yes", "No"], key='physical_activity')
    eats_fruits = st.selectbox("Does the patient consume at least 1 fruit per day?", ["Yes", "No"], key='eats_fruits')
    eats_veggies = st.selectbox("Does the patient consume vegetables at least once per day?", ["Yes", "No"], key='eats_veggies')
    heavy_drinker = st.selectbox("Does the patient consume 14 drinks or more per week (male) or 7 drinks or more per week (female)?", ["Yes", "No"], key='heavy_drinker')
    has_healthcare_cov = st.selectbox("Does the patient have any kind of health care coverage?", ["Yes", "No"], key='has_healthcare_cov')
    no_attention_bc_cost = st.selectbox("In the past 12 months, was the patient unable to see a doctor due to cost?", ["Yes", "No"], key='no_attention_bc_cost')
    walking_difficulty = st.selectbox("Does the patient have serious difficulty walking or climbing stairs?", ["Yes", "No"], key='walking_difficulty')
    is_male = st.selectbox("What gender was the patient assigned at birth?", ["Male", "Female"], key='is_male')

    # Non-binary questions
    bmi = st.number_input("What is the patient's Body Mass Index (BMI)?", min_value=10, max_value=90, step=1, key='bmi')
    general_health_score_level_groups = ["Excellent", "Very Good", "Good", "Fair", "Poor"]
    general_health_score = st.selectbox("How would the patient describe their health level?", general_health_score_level_groups, key='general_health_score')
    mental_health_bad_days = st.slider("How many days of bad mental health has the patient had in the last 30 days", 0, 30, key='mental_health_bad_days')
    physical_health_bad_days = st.slider("How many days of physical illness or injury has the patient had in the last 30 days", 0, 30, key='physical_health_bad_days')
    age_groups = ['18 to 24', '25 to 29', '30 to 34', '35 to 39', '40 to 44', '45 to 49', '50 to 54', '55 to 59', '60 to 64', '65 to 69', '70 to 74', '75 to 79', '80+']
    age = st.selectbox("What is the age of the patient?", age_groups, key='age')
    education_level_groups = ['Never attended school or only kindergarten', 'Elementary education', 'Some high school', 'High school graduate', 'College 1 year to 3 years', 'College graduate and above']
    education = st.selectbox("What is the highest level of education obtained by the patient?", education_level_groups, key='education')
    income_level_groups = ['Less than $10,000', '$10,001 to $20,000', '$20,001 to $30,000', '$30,001 to $40,000', '$40,001 to $50,000', '$50,001 to $60,000', '$60,001 to $70,000', '$70,001 or more']
    income = st.selectbox("What is the patient's income level?", income_level_groups, key='income')

    # Collecting and creating a pandas DataFrame when the user clicks Submit
    if st.button("Submit"):
        # Transform answers into values that can be processed by the model
        user_data = {
            "Has_high_bp": 1 if has_high_bp == "Yes" else 0,
            "Has_high_cholesterol": 1 if has_high_cholesterol == "Yes" else 0,
            "Checked_cholesterol": 1 if checked_cholesterol == "Yes" else 0,
            "BMI": bmi,
            "Is_smoker": 1 if is_smoker == "Yes" else 0,
            "Had_stroke": 1 if had_stroke == "Yes" else 0,
            "Has_heart_disease": 1 if has_heart_disease == "Yes" else 0,
            "Physical_activity": 1 if physical_activity == "Yes" else 0,
            "Eats_fruits": 1 if eats_fruits == "Yes" else 0,
            "Eats_veggies": 1 if eats_veggies == "Yes" else 0,
            "Heavy_drinker": 1 if heavy_drinker == "Yes" else 0,
            "Has_healthcare_cov": 1 if has_healthcare_cov == "Yes" else 0,
            "No_attention_bc_cost": 1 if no_attention_bc_cost == "Yes" else 0,
            "General_health_score": general_health_score_level_groups.index(general_health_score) + 1,
            "Mental_health_bad_days": mental_health_bad_days,
            # "Physical_health_bad_days": physical_health_bad_days,  #This variable is excluded as it was deleted during pre-processing
            "Walking_difficulty": 1 if walking_difficulty == "Yes" else 0,
            "Is_male": 1 if is_male == "Male" else 0,
            "Age": age_groups.index(age) + 1,
            "Education": education_level_groups.index(education) + 1,
            "Income": income_level_groups.index(income) + 1
        }

        # Create a pandas dataframe that can be processed by th emodel
        user_data_df = pd.DataFrame([user_data])
        st.write("Collected Data:")
        st.dataframe(user_data_df)

        proba_predicted = pickled_pipe.predict_proba(user_data_df)
        st.write(proba_predicted)


if __name__ == "__main__":
    main()



