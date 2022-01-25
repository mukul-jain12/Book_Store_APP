"""
    @File :   main.py
    @Author : mukul
    @Date :   20-01-2022
"""
import uvicorn
from fastapi import FastAPI
from routers import user_apis, book_apis, wishlist_apis

app = FastAPI(title="Book Store App")

app.include_router(user_apis.route)
app.include_router(book_apis.route)
app.include_router(wishlist_apis.route)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
