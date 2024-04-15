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
my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")

# Create a dropdown menu for the user to select a sweatsuit color or style
color_or_style = st.selectbox( 
    "Select a sweatsuit color or style",
    my_dataframe.select(col("color_or_style")).distinct().collect(),
    label_visibility="hidden"
)

pd_df = my_dataframe.to_pandas()

# Add an image of the selected product
st.image(pd_df[pd_df["color_or_style"] == color_or_style]["direct_url"].values[0])

# Add the price of the selected product to the app
st.write(
    f"Price: ${pd_df[pd_df['color_or_style'] == color_or_style]['price'].values[0]}"
)

# Add the sizes available for the selected product to the app
st.write(
    f"Sizes available: {pd_df[pd_df['color_or_style'] == color_or_style]['size_list'].values[0]}"
)

# Add the upsell message to the app
st.write(
    pd_df[pd_df['color_or_style'] == color_or_style]['upsell_product_desc'].values[0]
)
