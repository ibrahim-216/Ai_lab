import streamlit as st

# Set up Streamlit page
st.set_page_config(page_title="Temperature Converter", layout="centered")

# Title
st.title("🌡 Temperature Converter")
st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin.")

# User Input for Temperature
temperature = st.number_input("Enter Temperature Value:", format="%.2f")

# Dropdown for Selecting Input and Output Units
col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From Unit:", ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"])

with col2:
    to_unit = st.selectbox("To Unit:", ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"])

# Conversion Logic
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value  # No conversion needed

    # Convert from input unit to Celsius
    if from_unit == "Fahrenheit (°F)":
        value = (value - 32) * 5/9
    elif from_unit == "Kelvin (K)":
        value = value - 273.15

    # Convert from Celsius to output unit
    if to_unit == "Fahrenheit (°F)":
        return (value * 9/5) + 32
    elif to_unit == "Kelvin (K)":
        return value + 273.15
    return value  # Celsius remains unchanged

# Convert Button
if st.button("Convert"):
    converted_value = convert_temperature(temperature, from_unit, to_unit)
    st.success(f"🌡 {temperature} {from_unit} = {converted_value:.2f} {to_unit}")

# Footer
st.markdown("### 📌 Supports Celsius, Fahrenheit, and Kelvin conversions.")
