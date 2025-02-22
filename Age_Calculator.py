import streamlit as st
from datetime import datetime

# Custom CSS to modify the appearance
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: white;
    }
    .stButton>button {
        background-color: #FF6F61;
        color: white;
        font-size: 18px;
    }
    .stTextInput>div>div>input {
        background-color: #333333;
        color: white;
    }
    .stTextInput>label {
        color: white;
    }
    .stDateInput>label {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Set the title of the app
st.title("Age Calculator")

# Input: Date of Birth
dob = st.date_input("Select your date of birth")

# Function to calculate age
def calculate_age(dob):
    today = datetime.today().date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

# Calculate the age when a date of birth is selected
if dob:
    age = calculate_age(dob)
    st.write(f"Your age is: {age} years old")
