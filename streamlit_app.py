# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests 

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")
st.write(
    """Pick a sweatsuit color or style:
    """
)

cnx = st.connection("snowflake")
session = cnx.session()
my_cur = cnx.cursor() 
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()") 
my_data_row = my_cur.fetchone() 
st.text("Hello from Snowflake:") 
st.text(my_data_row)
