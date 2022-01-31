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
