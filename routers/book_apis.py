"""
    @File :   book_apis.py
    @Author : mukul
    @Date :   24-01-2022
"""
from logger import logging
from service.book_service import *
from schemas.books import Books
from fastapi import APIRouter, UploadFile, File

route = APIRouter(tags=["BOOKS"])


@route.get("/books/")
def get_all_users_details():
    """
        desc: created api to get all the books detail.
        return: books detail in SMD format.
    """
    try:
        book_details = retrieve_all_books()
        logging.info("Successfully Get All Books Details")
        logging.debug(f"Book Details are : {book_details}")
        return {"status": 200, "message": "Successfully Get All Books Details", "data": book_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@route.get("/book/", )
def get_book_details(book_id: int):
    """
        desc: created api to get a book details.
        param: book_id: it is a book id.
        return: book details in SMD format.
        """
    try:
        book_details = retrieve_book(book_id)
        logging.info("Successfully Get A Book Detail")
        logging.debug(f"Book Details are : {book_details}")
        return {"status": 200, "message": "Successfully Get A Book Details", "data": book_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@route.post("/book/", )
def add_new_book(books: Books):
    """
    desc: created api to add the book into book store app.
    param1: Books class which contains schema
    """
    try:
        book_details = add_book(books)
        logging.info("Book Successfully Added")
        logging.debug(f"Book Details are : {book_details}")
        return {"status": 200, "message": f"Successfully Added The Book!!", "data": book_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 402, "message": "Error : Book with this Id Already exist in database"}


@route.delete("/book/", )
def delete_book_details(book_id: int):
    """
    desc: created api to delete the book details using book id
    param: book_id: it is a book id
    return: b_id in SMD format
    """
    try:
        retrieve_book(book_id)
        b_id = delete_book(book_id)
        logging.info("Successfully Deleted The Book Details")
        logging.debug(f"Book ID is : {b_id}")
        return {"status": 204, "message": "Successfully Deleted The Book Details", "data": b_id}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@route.put("/book/", )
def update_book_details(book_id: int, books: Books):
    """
    desc: created api to update any book details
    param1: book_id: it is a user id
    param2: Books class which contains schema
    return: updated book details in SMD format
    """
    try:
        retrieve_book(book_id)
        book_details = update_book(book_id, books)
        logging.info("Successfully Updated The Book Details")
        logging.debug(f"Book Details are : {book_details}")
        return {"status": 200, "message": "Successfully Updated The Book Details", "data": book_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@route.post("/uploadFile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        detail = await insert_data_in_book(file)
        logging.info("Successfully Updated The Book Details")
        logging.debug(detail)
        return {"status": 200, "message": "Successfully Added The Book File"}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}
