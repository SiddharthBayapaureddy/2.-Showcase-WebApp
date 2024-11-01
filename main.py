import streamlit as st

#st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/pfp.png")

with col2:
    st.title('Siddharth')
    st.info('''
            Hey there! This is a Portfolio website showcasing all the apps, and projects I've worked on
            till now. Hope you like it! 
            :)
            ''')