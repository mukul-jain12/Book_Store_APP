"""
    @File :   db.py
    @Author : mukul
    @Date :   20-01-2022
"""
from logger import logging
import os

from dotenv import load_dotenv
from mysql.connector import connect, Error

load_dotenv()


class DBConnection:

    @staticmethod
    def establish_connection():
        """
            desc: Established database connection and perform query to created database
        """
        try:
            logging.info("Trying to establish the database connection")
            connection = connect(
                host=os.getenv('host'),
                user=os.getenv('user_name'),
                password=os.getenv('user_password'),
                database="book_store_app",
            )
            logging.info("Database Connection is Established")
            return connection
        except Error as e:
            logging.error("Connection not Established")
            return {"status": 502, "message": "Error : Connection not Established"}
