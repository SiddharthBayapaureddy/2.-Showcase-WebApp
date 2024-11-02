import smtplib
import ssl

def send_email(text):


    host = 'smtp.gmail.com'
    port = 465


    username = 'reallysiddhxrth@gmail.com'
    password = 'cbhogwyulugrdpgh'

    reciever = 'siddharthbayapureddy@gmail.com'

    my_context = ssl.create_default_context()

    message = text

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, reciever , message)
