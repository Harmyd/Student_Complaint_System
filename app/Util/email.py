from email.message import EmailMessage
from email.utils import formataddr
import smtplib
from fastapi import status
from fastapi.responses import JSONResponse

def send_email(code,receiver_email):
    my_email="abdulharmyd3@gmail.com"
    my_app_password="ughtbouqgtkdhpzl"

    msg= EmailMessage()
    msg["From"]=formataddr(("Univoice",my_email)) 
    msg["To"]=receiver_email
    msg["Subject"]="Password_Reset"
    msg.set_content(f"Here is your reset code {code},This code will expire in 1 minute")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.set_debuglevel(1)
            smtp.login(my_email,my_app_password)
            smtp.send_message(msg)
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message":str(e)}
        )