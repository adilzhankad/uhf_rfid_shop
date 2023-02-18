import smtplib
import ssl
from email.message import EmailMessage
import random

def sendemail(a):# Define email sender and receiver
    email_sender = 'rfid.kassa@gmail.com'
    email_password = 'qzpxgdcflnfbldan'
    email_receiver = a

    x = random.randint(1000,9999)
    # Set the subject and body of the email


    subject = str(x)
    body = "Nurasyl Krisa Diskord davey"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    return x