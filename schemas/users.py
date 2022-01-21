"""
    @File :   users.py
    @Author : mukul
    @Date :   20-01-2022
"""
from pydantic import BaseModel


class Users(BaseModel):
    user_name: str
    email_id: str
    password: str
    mobile_number: int
