import pandas as pd
import streamlit as st
import plotly.express as px



# st.header("WELCOME TO LESSON 18")
# df = pd.DataFrame({
#     "Name": ["Alma", "Blin", "Klea"],
#     "Age": [27, 17, 17],
#     "City": ["Ferizaj", "Podujeve", "Podujeve"]
# })
# st.dataframe(df)


books_df = pd.read_csv("bestsellers_with_categories_2022_03_27.csv")

st.sidebar.header("Add new book data")
with st.sidebar.form("book_form"):
    new_name=st.text_input("Book Name")
    new_name=st.text_input("Book Name")
    new_author=st.text_input("Author")
    new_user_rating=st.slider("user rating",0.0,5.0,0.0,0.1)
    new_reviews=st.number_input("Review", min_value=0,step=1)
    new_price=st.number_input("Price",min_value=0,step=1)
    new_year=st.number_input("Year",min_value=2009,max_value=2022,step=1)
    new_genre=st.selectbbox("Genre",filtered_df['Genre'].unique())
    submit_button=st.form_submit_button(label="Add new book")
if submit_button:
    new_data={
        "Name":new_name,
        "Author":new_author,
        "User Rating": new_user_rating,
        "Reviews":new_reviews,
        "Price":new_price,
        "Year":new_year,
        "Genre":new_genre
    }
    filtered_df=pd.contact([pd.DataFrame(new_data,index=[0]),filtered_df],ignore_index=True)
    filtered_df.to_csv("bestsellers_with_categories_2022_03_27.csv",index=False)
    st.sidebar.success("New book added")

st.sidebar.header("Filter Options:")
selected_author=st.sidebar.selectbox("Select Author",["All"]+list(filtered_df["Author"].unique()))
selected_genre=st.sidebar.selectbox("Select genre",["All"]+list(filtered_df["Genre"].unique()))
min_rating=st.sidebar.slider("Minimum User Rating",0.0,5.0,0.0,0.1)
max_price=st.sidebar.slider("Maximum price",0,books_df["Price"].max(),filtered_df["Price"].max())

filtered_df=filtered_df.copy()
if selected_author!="All":
    filtered_df=filtered_df[filtered_df["Author"]==selected_author]
if selected_author!="All":
    filtered_df=filtered_df[filtered_df["Year"]==int(selected_year)]
if selected_author!="All":
    filtered_df=filtered_df[filtered_df["Genre"]==selected_genre]
filtered_df=filtered_df[
    (filtered_df["User Rating"]>=min_rating)&(filtered_df["Price"]<=max_price)
]

st.title("Bestselling Books Analysis")
st.write("This app analyzes the Amazon top selling books from 2009 to 2022")


st.subheader("Summary Statistics")
total_books = filtered_df.shape[0]
unique_title = filtered_df["Name"].nunique()
ave_rating = filtered_df["User Rating"].mean()
ave_price = filtered_df["Price"].mean()


col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_title)
col3.metric("Avg Rating", ave_rating)
col4.metric("Average Price", ave_price)

st.header("Dataset Preview")
st.write(filtered_df.head())


col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = filtered_df["Name"].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors = filtered_df["Author"].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")
fig = px.pie(filtered_df, names="Genre", title="Most Liked Genre (2009-2022)", color="Genre", color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number of Fiction vs Non-Fiction Books Over the years")
size=filtered_df.groupby(['Year','Genre']).size().reset_index(name='Counts')
fig=px.bar(size,x='Year',y='Counts',color='Genre',title='Number of Fiction vs Non-Fiction books from 2009-2022')
st.plotly_chart(fig)

st.subheader("Top 15 authors by counts of books published (2009-2022)")
top_authors=filtered_df['Author'].value_counts().head(15).reset_index()
top_authors.columns=['Author', 'Count']
fig=px.bar(top_authors,x='Count',y='Author',orientation='h',
           title='Top 15 Authors by Counts of Books Published',
           labels={"Count": 'Counts of books published', 'Author': 'Author'},
           color='Count',color_countinuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Filter Data by Genre")
genre_filter=st.selectbox("Select Genre", filtered_df['Genre'].unique())
filtered_df =filtered_df[filtered_df['Genre']==genre_filter]
st.write(filtered_df)

