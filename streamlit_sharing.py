import streamlit as st
import pandas as pd
from gsheetsdb import connect
import config

st.title("My first Streamlit WebApp")


df = pd.DataFrame({"one":[1,2,3], "two":[4,5,6], "three":[7,8,9]})
st.write(df)


st.title("Connect to Google sheets")
gsheet_url = config.LINK
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)

#print(f'There are total of {bags * apples_in_bag} apples')
#"https://docs.google.com/spreadsheets/d/1tXtSdJUrDFdQ2w4tvwAoE1ZIhIecNKYMCp1z7xwLvQY/edit?usp=sharing"
