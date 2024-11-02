import streamlit as st 
from send_email import send_email

st.header('Contact Me!')

with st.form(key='form'):
    user_email = st.text_input('Enter your Email Address: ',
                               placeholder='Enter your email here...',
                               key='email')
    user_message = st.text_area('Enter your message: ',
                                placeholder='Tell me what I can improve on...',
                                key='message')
    message = f'''\
Subject: New email from {user_email}

From: {user_email}
{user_message}
'''
    submit_button = st.form_submit_button('Submit')
    if submit_button:
        send_email(message)
        st.info('Your email is sent! Thank you')
