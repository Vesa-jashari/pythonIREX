import streamlit as st

def calculate(nr1, nr2, operation):
    if operation == "Addition":
        result = nr1 + nr2
    elif operation == "Subtraction":
        result = nr1 - nr2
    elif operation == "Multiplication":
        result = nr1 * nr2
    elif operation == "Division":
        try:
            result = nr1 / nr2
        except ZeroDivisionError:
            result = "Cannot divide by zero"
    return result

def main():
    st.title("Simple calculator")
    nr1 = st.number_input("Enter first number", step=1)
    nr2 = st.number_input("Enter second number", step=1)
    operation = st.radio("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])
    result = calculate(nr1, nr2, operation)
    st.write(f"Result of {operation} of {nr1} and {nr2} is: {result}")

if __name__ == "__main__":
    main()


