import streamlit
streamlit.title('My Parents New Healthy Diner!')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega3 & blueberry oatmeal')
streamlit.text('🥗 Kale & Spinach & Rocket smoothie')
streamlit.text('🐔 Hard-boiled free range Eggs')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
