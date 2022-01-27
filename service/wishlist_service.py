"""
    @File :   wishlist_service.py
    @Author : mukul
    @Date :   24-01-2022
"""
from core.db import DBConnection

connection = DBConnection.establish_connection()
cursor = connection.cursor(buffered=True, dictionary=True)


def retrieve_wishlist(user_id):
    """
        desc: query to get all wishlist detail from database
        return: wishlist detail in dictionary format
    """
    get_wishlist_query = f"SELECT * FROM wishlist where user_id = {user_id}"
    cursor.execute(get_wishlist_query)
    wish_list = [i for i in cursor]
    if wish_list:
        return wish_list
    else:
        raise Exception("There is no result for the Wishlist.")


def add_to_wishlist(user_id, wishlist):
    """
        desc: query to insert book details in wishlist
        param: user_id, wishlist model.
    """
    show_data_query = "INSERT INTO wishlist (user_id, book_id) VALUES(%d, %d)" % (user_id, wishlist.book_id)
    cursor.execute(show_data_query)
    connection.commit()
    return "Book Successfully Added in Wishlist"


def remove_book(user_id, book_id):
    """
        desc: query to delete book details from wishlist
        param: id: book id, which you want to delete.
        return: book id which is deleted from wishlist
    """
    show_data_query = f"delete from wishlist where book_id = {book_id} and user_id in({user_id})"
    cursor.execute(show_data_query)
    connection.commit()
    return book_id
