### App to show the demonstrate the model saved in a pkl file

### import libraries
import pandas as pd
import streamlit as st
import joblib

# basic function to write text on app
st.write('Streamlit is an open-source app framework for Machine Learning and Data Science teams. For the docs, please click [here](https://docs.streamlit.io/en/stable/api.html). \
    This is is just a very small window into its capabilities.')


#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file



#######################################################################################################################################
### Create a title

#Let's write a title to be displayed in the app
st.title("The Best App Ever")

## You can also use markdown syntax using st.write("#...") 
st.write("### App for investigating NYC bikes")

### To position text and color, you can use html syntax
st.markdown("<h1 style='text-align: center; color: blue;'>The best ever morning kickoff</h1>", unsafe_allow_html=True)


#######################################################################################################################################
### DATA LOADING

#defining function to load data
def load_data(path, num_rows):
    df = pd.read_csv(path, nrows=num_rows)

    # Streamlit will only recognize 'latitude' or 'lat', 'longitude' or 'lon', as coordinates
    # So we need to rename our columns "Start Station Latitude" and "Start Station Longitude" 
    # so that streamlit will detect these columns for displaying maps later
    df.rename(columns= {"Start Station Latitude": "lat", "Start Station Longitude": "lon"}, inplace= True)

    # From our prior knowledge of this dataset suppose we also want to change the datatype of 'Start Time'
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # Now we return the loaded data frame
    return df

# Load first 50K rows
df = load_data("NYC_bikes_small.csv", 50000)

# Display the dataframe in the app
st.dataframe(df)
#######################################################################################################################################
### STATION MAP
st.subheader("Map of data")

st.map(df)

#######################################################################################################################################
### DATA ANALYSIS & VISUALIZATION
# Now we want to display a bar chart of "Daily usage per hour" BUT we want to be able to filter to include either all trips or
# only ROUND TRIPS.

# To do this we create a sidebar with a checkbox first and then make the barchart

###  Add filter on side bar after initial bar chart constructed
st.sidebar.subheader("Usage filters")
round_trip = st.sidebar.checkbox('Round trips only')

# changes df based on what user has checked in the checkbox
if round_trip:
    df = df[df['Start Station ID'] == df['End Station ID']]


# NOTE about checkboxes ---> When the user changes the checkbox, this .py file is rerun FROM TOP TO BOTTOM and the app rerendered.
# This means changing the filter (which in the code below alters the varible df) any changes to df will only show in anything after
# the if statement (in this example ONLY the barchart and not anything that used df above!)

# Now adding the barchart section
st.subheader("Daily usage per hour")

counts = df["Start Time"].dt.hour.value_counts()
st.bar_chart(counts)

### The features we have used here are very basic. Most Python libraries can be imported as in Jupyter Notebook so the possibilities are vast.
#### Visualizations can be rendered using matplotlib, seaborn, plotly etc.
#### Models can be imported using *.pkl files (or similar) so predictions, classifications etc can be done within the app using previously optimized models
#### Automating processes and handling real-time data


#######################################################################################################################################
### MODEL INFERENCE
# Subheader:
st.subheader("Play with the sentiment model")

# Load the model using joblib
model = joblib.load("sentiment_pipeline.pkl")

# Set up input field with st.text_input()
text = st.text_input("Enter Your Review Here", "Best Bike trip ever")

# Use the model to predict sentiment & save to a variable called prediction NOTE the use of {} brackets around "text"
prediction = model.predict({text})

# based on prediction display something to user
if prediction == 1:
    st.write("## Postive Sentiment")
else:
    st.write("## Negative Sentiment")



#######################################################################################################################################
### Streamlit Advantages and Disadvantages
    
st.subheader("Streamlit Advantages and Disadvantages")
st.write('**Advantages**')
st.write(' - Easy, Intuitive, Pythonic')
st.write(' - Free!')
st.write(' - Requires no knowledge of front end languages')
st.write('**Disadvantages**')
st.write(' - Apps all look the same')
st.write(' - Not very customizable')
st.write(' - A little slow. Not good for MLOps, therefore not scalable')