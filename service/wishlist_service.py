"""
    @File :   wishlist_service.py
    @Author : mukul
    @Date :   24-01-2022
"""
from core.db import DBConnection

connection = DBConnection.establish_connection()
cursor = connection.cursor(buffered=True, dictionary=True)


def retrieve_wishlist():
    """
        desc: query to get all wishlist detail from database
        return: wishlist detail in dictionary format
    """
    get_wishlist_query = "SELECT * FROM wishlist"
    cursor.execute(get_wishlist_query)
    wish_list = [i for i in cursor]
    if wish_list:
        return wish_list
    else:
        raise Exception("There is no result for the Wishlist.")


def add_to_wishlist(user_id, book_id, wishlist):
    """
        desc: query to insert book details in database
        param: author_name, title, image, quantity, price, description.
        return: book detail in dictionary format
    """
    show_data_query = "INSERT INTO wishlist (user_id, book_id, book_name) " \
                      "VALUES(%d, %d, '%s')" % \
                      (user_id, book_id, wishlist.book_name)
    cursor.execute(show_data_query)
    connection.commit()
    return wishlist