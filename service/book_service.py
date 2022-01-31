"""
    @File :   book_service.py
    @Author : mukul
    @Date :   23-01-2022
"""
from io import StringIO

from fastapi import UploadFile

from core.db import DBConnection
import pandas as pd

connection = DBConnection.establish_connection()
cursor = connection.cursor(buffered=True, dictionary=True)


def retrieve_all_books():
    """
        desc: query to get all book detail from database
        return: books detail in dictionary format
    """
    get_books_query = "SELECT * FROM books"
    cursor.execute(get_books_query)
    connection.commit()
    books = [i for i in cursor]
    if books:
        return books
    else:
        raise Exception("There is no result for the book.")


def retrieve_book(book_id: int):
    """
        desc: query to get a book detail from database
        param: book_id: id for a particular book
        return: book detail in dictionary format
    """
    show_data_query = f"SELECT * FROM books WHERE id={book_id}"
    cursor.execute(show_data_query)
    connection.commit()
    book = [i for i in cursor]
    if book:
        return book
    else:
        raise Exception("Book with this Id doesn't exist in the Database!")


def add_book(books):
    """
        desc: query to insert book details in database
        param: author_name, title, image, quantity, price, description.
        return: book detail in dictionary format
    """
    show_data_query = "INSERT INTO books (author_name, title, image, quantity, price, description) " \
                      "VALUES('%s', '%s', '%s', %d, %d, '%s')" % \
                      (books.author_name, books.title, books.image, books.quantity, books.price, books.description)
    cursor.execute(show_data_query)
    connection.commit()
    return books


def delete_book(book_id):
    """
        desc: query to delete book details from database
        param: id: book id, which you want to delete.
        return: book id which is deleted from db
    """
    show_data_query = f"delete from books where id = {book_id}"
    cursor.execute(show_data_query)
    connection.commit()
    return book_id


def update_book(book_id, books):
    """
        desc: query to update book details in database
        param: book_id, author_name, title, image, quantity, price, description.
        return: book detail in dictionary format
    """
    show_data_query = "UPDATE books SET author_name = '%s', title = '%s', image = '%s', quantity = %d, price = %d, " \
                      "description = '%s' WHERE id = %d" % (books.author_name, books.title, books.image,
                                                            books.quantity, books.price, books.description, book_id)
    cursor.execute(show_data_query)
    connection.commit()
    book_data = retrieve_book(book_id)
    return book_data


async def insert_data_in_book(file):
    """
        desc: query to insert book details in database
        param: author_name, title, image, quantity, price, description.
        return: book detail in dictionary format
    """
    books_dataframe = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-8')
    column_name = ", ".join([str(i) for i in books_dataframe.columns.tolist()])
    for i, rows in books_dataframe.iterrows():
        sql = "INSERT INTO books (" + column_name + ") VALUES (" + "%s," * (len(rows)-1) + "%s)"
        cursor.execute(sql, tuple(rows))
        connection.commit()
    return "Books are Added Successfully!!"
