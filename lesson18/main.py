import pandas as pd
import streamlit as st
import plotpy.express as px

# st.header("WELCOME TO LESSON 18")
# df=pd.DataFrame({
#     "Name":["Alma"."Blin","Klea"]
#     "Age":[27,17,17],
#     "city":["Ferizaj", "Podujeve","Podujeve"]
# })
# st.dataframe(df)

books_df=pd.read_csv("bestsellers_with_categories_2022_03_27.csv")
st.title("Bestselling books Analysis")
st.write("this app analyzes the amazon top selling books from 2009 to 2022")

st.subheader("summary statics")
total_books=books_df.shape[0]
unique_title=books_df["Name"].nunique()
ave_rating=books_df["User Rating"].mean()
ave_price=books_df["Price"].mean()

col1,col2,col3,col4.columns(4)
col1.metric("Total Books",total_books)
col2.metric("Unique Titles",unique_title)
col3.metric("Ave Rating",ave_rating)
col4.metric("Average price",ave_price)