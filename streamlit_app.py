# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests 
import pandas as pd 

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")

cnx = st.connection("snowflake")
my_cur = cnx.cursor() 

# run a snowflake query and put it all in a var called my_catalog 
my_cur.execute("select color_or_style from catalog_for_website") 
my_catalog = my_cur.fetchall() 

# put the dafta into a dataframe 
df = pd.DataFrame(my_catalog) 

# temp write the dataframe to the page so I Can see what I am working with 
# st.write(df) 

# put the first column into a list 
color_list = df[0].values.tolist() 

# print(color_list) 

# Let's put a pick list here so they can pick the color 
option = st.selectbox('Pick a sweatsuit color or style:', list(color_list)) 

# We'll build the image caption now, since we can 
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!' 

# use the option selected to go back and get all the info from the database
my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';") 
df2 = my_cur.fetchone() 

st.image( df2[0], width=400, caption= product_caption ) 
st.write('Price: ', df2[1]) 
st.write('Sizes Available: ',df2[2]) 
st.write(df2[3])

my_cur.close()


