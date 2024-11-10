import streamlit as st

with st.container():
    st.header("This is a contaioner")
    st.write("This is inside the container")
    st.write("Outside the container")





st.sidebar.header("Sidebar")
st.sidebar.write("This is the sidebar")
st.sidebar.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.sidebar.radio("Go to", ["Home", "Data", "Settings"])
with st.form("my_form", clear_on_submit=True):
    name = st.text_input("Name")
    age = st.slider("Age", min_value=0, max_value=100)
    email = st.text_input("Email")
    biography = st.text_area("Short Bio")
    terms = st.checkbox("I agree to the terms and conditions")

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Email: {email}")
    st.write(f"Biography: {biography}")

    if terms:
        st.write("You have agreed to the terms and conditions")
    else:
        st.write("You did not agree to the terms and conditions")






tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

# Tab 1 content
with tab1:
    st.header("Tab 1")
    st.write("This is the content for Tab 1")
    st.button("Click me on Tab 1")

# Tab 2 content
with tab2:
    st.header("Tab 2")
    st.write("This is the content for Tab 2")
    st.slider("Select a value", 0, 100, 50)

# Tab 3 content
with tab3:
    st.header("Tab 3")
    st.write("This is the content for Tab 3")
    st.text_area("Write something in Tab 3")
