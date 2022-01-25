"""
    @File :   wishlist_apis.py
    @Author : mukul
    @Date :   24-01-2022
"""
from logger import logging
from service.wishlist_service import *
from schemas.wishlist import Wishlist
from fastapi import APIRouter, Header
from jwt_token.generate_token import *
route = APIRouter(tags=["WISHLIST"])


@route.get("/wishlist/")
def get_all_wishlist():
    """
            desc: created api to get a user details.
            param: user_id: it is a user id.
            return: user details in SMD format.
            """
    try:
        wish_list = retrieve_wishlist()
        logging.info("Successfully Get All Books From Wishlist")
        logging.debug(f"User Details are : {wish_list}")
        return {"status": 200, "message": "Successfully Get A Wishlist", "data": wish_list}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@route.post("/wishlist/")
def add_books_to_wishlist(wish: Wishlist, token: str = Header(None)):
    """
    desc: created api to add book to wishlist into book store app.
    param1: Users class which contains schema
    return: user_token in SMD format
    """
    try:
        user_id = decode_login_token(token)
        wish_list = add_to_wishlist(user_id, wish)
        logging.info("Book Successfully Added To wishlist")
        return {"status": 200, "message": f"Book Successfully Added To wishlist!!", "data": wish_list}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 402, "message": f"Error : {e}"}
