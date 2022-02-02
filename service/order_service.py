"""
    @File :   order_service.py
    @Author : mukul
    @Date :   29-01-2022
"""
from core.db import DBConnection

connection = DBConnection.establish_connection()
cursor = connection.cursor(buffered=True, dictionary=True)


def book_order(user_id, order):
    """
        desc: query to call the procedure where many queries are performed
        param: user_id, order model.
    """
    args = [user_id, f'{order.address}']
    show_data_query = cursor.callproc('place_order', args)
    connection.commit()
    return show_data_query


def retrieve_user_order(user_id: int):
    """
        desc: query to get all order detail from database
        param: user_id: encoded from the
        return: order detail in dictionary format
    """
    show_data_query = f"SELECT order_item.id, user_id, order_id, order_item.quantity, books.title, books.author_name," \
                      f"books.price FROM order_item INNER JOIN books on books.id = order_item.book_id WHERE user_id =" \
                      f" %d" % user_id
    cursor.execute(show_data_query)
    connection.commit()
    order = [i for i in cursor]
    if order:
        return order
    else:
        raise Exception("User not ordered any book from the book.")
