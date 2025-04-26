import streamlit as st   # We are using Streamlit to make the web app

# ---- App Title ----
st.title("🏋️ Simple BMI Calculator")  # Shows the title at the top of the page

# ---- User Input Fields ----
# Asking user to enter weight and height
weight = st.number_input("Enter your weight (in kilograms)", min_value=0.0, step=0.1)
height = st.number_input("Enter your height (in meters)", min_value=0.0, step=0.01)

# ---- Button to Calculate BMI ----
if st.button("Calculate BMI"):
    
    # Check if height is zero (to avoid error)
    if height == 0:
        st.error("Height cannot be zero!")  # Show error if height is 0
        
    else:
        # Calculate BMI using formula
        bmi = weight / (height ** 2)  # BMI = weight divided by (height × height)
        
        # Show the BMI result
        st.success(f"Your BMI is: {bmi:.2f}")  # Show BMI with 2 decimal points
        
        # ---- Show BMI Category ----
        if bmi < 18.5:
            st.info("Category: Underweight")  # If BMI is less than 18.5
        elif 18.5 <= bmi < 24.9:
            st.info("Category: Normal weight")  # If BMI is between 18.5 and 24.9
        elif 25 <= bmi < 29.9:
            st.info("Category: Overweight")  # If BMI is between 25 and 29.9
        else:
            st.info("Category: Obese")  # If BMI is 30 or more

# ---- Footer Text ----
st.caption("Developed by Ibad using Streamlit")  # Small text at the bottom of the page