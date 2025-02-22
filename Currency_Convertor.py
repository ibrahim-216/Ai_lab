import streamlit as st

# Exchange rates (example rates, can be updated with an API for real-time data)
exchange_rates = {
    "PKR": 1,         # Base currency
    "USD": 0.0036,    # Example: 1 PKR = 0.0036 USD
    "EUR": 0.0033,    # Example: 1 PKR = 0.0033 EUR
    "GBP": 0.0028,    # Example: 1 PKR = 0.0028 GBP
    "INR": 0.30       # Example: 1 PKR = 0.30 INR
}

# Custom CSS for dark theme with larger button size and label color change
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: white;
    }
    .stApp {
        background-color: #121212;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #f1c40f;
        text-align: center;
    }
    .stSelectbox, .stNumberInput {
        background-color: #333333;
        color: white;
        border-radius: 5px;
    }
    .stSelectbox>label, .stNumberInput>label {
        color: #FF6F61;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #FF6F61;
        color: white;
        border-radius: 10px;
        padding: 15px 40px;
        font-size: 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #e74c3c;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.title("💱 Currency Converter")
st.subheader("Convert between PKR, USD, EUR, GBP, and INR")

# User Input
amount = st.number_input("Enter Amount:", min_value=0.0, value=100.0, format="%.2f")
from_currency = st.selectbox("From Currency", list(exchange_rates.keys()))
to_currency = st.selectbox("To Currency", list(exchange_rates.keys()))

# Conversion Logic
if st.button("Convert 💵"):
    if from_currency != to_currency:
        converted_amount = (amount / exchange_rates[from_currency]) * exchange_rates[to_currency]
        st.success(f"✅ {amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        st.warning("❗ Select different currencies to convert.")

# Footer
st.markdown("<hr><center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)
