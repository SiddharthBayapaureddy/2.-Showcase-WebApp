import streamlit as st
import pandas 

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/pfp.png", width=500  )

with col2:
    st.title('Siddharth')
    st.info('''
            Hey there! This is a Portfolio website showcasing all the apps, and projects I've worked on
            till now. Hope you like it! 
            :)
            ''')
content = '''
Below you can find some apps I have built in Python. Feel free to check them out and contact me!
'''
st.write(content)


df = pandas.read_csv('data.csv' , sep=';')

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.info(row['description'])
        photo = f'images/{row['image']}'
        st.image(photo)
        st.write(f"[Source Code]({row['url']})")    
       
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.info(row['description'])
        photo = f'images/{row['image']}'
        st.image(photo)
        st.write(f"[Source Code]({row['url']})")
        