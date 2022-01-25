"""
    @File :   email_service.py
    @Author : mukul
    @Date :   23-01-2022
"""
import os
from dotenv import load_dotenv
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv('mail_username'),
    MAIL_PASSWORD=os.getenv('mail_password'),
    MAIL_FROM=os.getenv('mail_from'),
    MAIL_PORT=587,
    MAIL_SERVER=os.getenv('mail_server'),
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


async def send_mail(email: str, token_id: str):
    template = f"""
    Hello,
    
    you have registered to Book Store App. To verify click here
    <a href="http://127.0.0.1:8000/user/verification/{token_id}"><button>Click Here To Verfiy</button></a>
    """

    message = MessageSchema(
        subject="Account Verification: Book Store App",
        recipients=[email],
        body=template,
        subtype='html'
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    return "Verification mail has been sent to your mail id"
