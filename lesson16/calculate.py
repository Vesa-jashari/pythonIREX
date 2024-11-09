import streamlit as st

def calculate(nr1, nr2, operation):
    if operation=="Addition":
        result=nr1=nr2
    if operation=="Subtraction":
        result=nr1-nr2
    if operation=="Multiplication":
        result=nr1*nr2
    if operation=="Division":
        try:
            result=nr1/nr2
        except ZeroDivisionError:
            result="Cannot divide by zero"
    return result

def main():
    st.title("Simple calculator")
    nr1=st.number_input("Enter first number",step=1)
    nr2=st

