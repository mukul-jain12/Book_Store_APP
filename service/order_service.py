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
    show_data_query = "call order_book(%d, '%s')" % (user_id, order.address)
    cursor.execute(show_data_query)
    connection.commit()
    return "Book Successfully Ordered"
