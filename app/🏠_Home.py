# Run this code to start the app:
# streamlit run 🏠_Home.py

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

# Top section of the home page
st.title("Early Disease Detection System")
st.subheader("Diabetes risk predictor developed by Diego Villanueva")

# Divide page in 2 columns
col1, col2 = st.columns(2)

# Right hand column

# Left hand column
with col1:
    st.write("""
    **Problem:** \n
    Diabetes has become one of the biggest epidemics in human history, yet efforts in early detection are lagging behind.

    **Solution:** \n
    An early warning system, powered by machine learning, that helps doctors to predict the risk of a patient developing diabetes.

    **Impact:**\n
    - Improve management and treatment
    - Prevent complications
    - Avoid or reverse disease
    """)

with col2:
    st.image('Dr_using_app.png', caption='Early Disease Detection System')

# In the right column, add an image
