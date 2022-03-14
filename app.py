import streamlit as st
import numpy as np
import pandas as pd
st.title("we will learn")
st.header("This is header")
st.subheader("This is subheader")
st.text("Text")
#for multiple columns
first,last = st.columns(2)
firstname = first.text_input("Enter your first name")
lastname = last.text_input("Enter your last name")
st.write(firstname)
st.write(lastname)
df = np.random.rand(20,3)
df
st.table(df) 
st.dataframe(df)
area = st.text_area("Enter your words")
dfs=pd.DataFrame(df)
st.dataframe(dfs.style.highlight_max(axis = 1))
dfa = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)
st.dataframe(dfa.style.highlight_max(axis = 1))
#graph
#line chart
st.line_chart(dfa)

#barchart 
st.bar_chart(dfa)
#map
#upload image 
img = st.file_uploader("upload your file")
#show image
if img:
  st.image(img)
#input 
#text input
# number input
#name = st.text_input("Entere Your Name")
#st.write(name)
#number = st.number_input("Enter YOur age")
#st.write(number)