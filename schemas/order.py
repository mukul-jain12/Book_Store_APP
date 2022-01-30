"""
    @File :   order.py
    @Author : mukul
    @Date :   29-01-2022
"""
from pydantic import BaseModel


class Order(BaseModel):
    address: str
