"""
    @File :   cart.py
    @Author : mukul
    @Date :   27-01-2022
"""
from pydantic import BaseModel


class Cart(BaseModel):
    book_id: int
