from email.message import EmailMessage
import smtplib

def send_email(code,receiver_email):
    my_email="abdulharmyd3@gmail.com"
    my_app_password="gwoy xkjq itic ooqm"

    msg= EmailMessage()
    msg["From"]=my_email
    msg["To"]=receiver_email
    msg["Subject"]="Password_Reset"
    msg.set_content(f"Here is your reset code {code}")

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(my_email,my_app_password)
        smtp.send_message(msg)