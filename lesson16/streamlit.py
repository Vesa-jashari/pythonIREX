import streamlit as st

def main():
    st.title("Hello , from Streamlit")
   if  st.button("Click me!!"):
       st.write("Button clicked")
   if  st.checkbox("Check me"):
       st.write("You're seeing thid text because you chedk the checkbox")

   user_input_text=st.text_input("Enter text","Sample")
   st.write("you entered: ", user_input_text)
   user_input_number=st.number_input("Enter your age", min_value=0,max_value=100)
   st.write("you input:", user_input_number)
   user_input_textarea=st.text.area("Enter your message")
   st.write(f"Message:{user_input_textarea}")
   user_input_radio=st.radio("Pick one", ["Opsioni1", "Opsioni2", "Opsioni3"])
   st.write(f"You choose:{user_input_radio}")
   if st.button("Success"):
       st.error("Operation was successful")


   if __name__=="__main__":
         main()