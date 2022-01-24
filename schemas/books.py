"""
    @File :   books.py
    @Author : mukul
    @Date :   23-01-2022
"""
from pydantic import BaseModel


class Books(BaseModel):
    author_name: str
    title: str
    image: str
    quantity: int
    price: int
    description: str
