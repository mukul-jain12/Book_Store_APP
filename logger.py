"""
    @File :   logger.py
    @Author : mukul
    @Date :   20-01-2022
"""
import logging

logging.basicConfig(filename='F:/CFP/BookStoreApp/book_store_app.log', filemode='a', level=logging.DEBUG,
                   format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')
