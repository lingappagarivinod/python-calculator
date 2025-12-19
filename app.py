import streamlit as st

st.title("Python Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate"):
    if operation == "Addition":
        st.success(num1 + num2)

    elif operation == "Subtraction":
        st.success(num1 - num2)

    elif operation == "Multiplication":
        st.success(num1 * num2)

    elif operation == "Division":
        if num2 != 0:
            st.success(num1 / num2)
        else:
            st.error("Division by zero not allowed")
