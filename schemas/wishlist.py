"""
    @File :   wishlist.py
    @Author : mukul
    @Date :   24-01-2022
"""
from pydantic import BaseModel


class Wishlist(BaseModel):
    book_id: int
