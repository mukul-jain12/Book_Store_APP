"""
    @File :   wishlist_apis.py
    @Author : mukul
    @Date :   24-01-2022
"""
from logger import logging
from service.wishlist_service import *
from schemas.wishlist import Wishlist
from routers.user_apis import verify_token
from fastapi import APIRouter, Depends

route = APIRouter(tags=["WISHLIST"])


@route.get("/wishlist/")
def get_all_wishlist(token=Depends(verify_token)):
    """
        desc: created api to get a wishlist for user.
        param: user_id: it is a user id.
        return: book details from wishlist in SMD format.
    """
    try:
        user_id = token
        wish_list = retrieve_wishlist(user_id)
        logging.info("Successfully Get All Books From Wishlist")
        logging.debug(f"User Details are : {wish_list}")
        return {"status": 200, "message": "Successfully Get A Wishlist", "data": wish_list}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@route.post("/wishlist/")
def add_books_to_wishlist(wishlist: Wishlist, token=Depends(verify_token)):
    """
    desc: created api to add book to wishlist into book store app.
    param1: Wishlist class which contains schema
    return: success message in SMD format
    """
    try:
        user_id = token
        wish_list = add_to_wishlist(user_id, wishlist)
        logging.info("Book Successfully Added To wishlist")
        return {"status": 200, "message": f"Book Successfully Added To wishlist!!", "data": wish_list}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 402, "message": f"Error : {e}"}


@route.delete("/wishlist/")
def delete_books_from_wishlist(wishlist: Wishlist, token=Depends(verify_token)):
    """
    desc: created api to remove book from wishlist.
    param1: Wishlist class which contains schema
    return: book_id in SMD format
    """
    try:
        user_id = token
        wish_list = remove_book(user_id, wishlist)
        logging.info("Book Successfully Removed From wishlist")
        return {"status": 200, "message": f"Book Successfully Removed From wishlist!!", "data": wish_list}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 402, "message": f"Error : {e}"}
