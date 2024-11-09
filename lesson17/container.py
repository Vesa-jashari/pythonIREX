# import streamlit as st
# with st.container():
#     st.header("This is a contaioner")
#     st.write("This is inside the container")
#     st.write("Outside the container")
from turtle import st

st.sidebar.header("Sidebar")
st.sidebar.write("this is sidebar")
st.sidebar.selectbox("Choose an option", ["Option 1", "option 2", "option 3"])
st.sidebar.radio("Go to ",["Home","Data","Setting"])

with st.form("my_form", clear_on_sumbit=True):
    name=st.text_input("Name")
    age=st.slider("Age", min_value=0,max_value=100)
    email=st.text_input("Email")
    biography=st.text_area("Short Bio")
    terms=st.checkbox("i agree the terms and conditions")
if submit_button:
    st.write(f"Name:{name}")
    st.write(f"Age:{age}")
    if terms:
        st.write("You have agreed to the terms and conditions")
    else:
        st.write("you did not agree to terms and conditions")



tab1,tab2,tab3=st.tabs(["Tab 1", "Tab 2","Tab 3"])

with tab1:
    st.header("Tab1")
    st.write("content")

with tab2:

