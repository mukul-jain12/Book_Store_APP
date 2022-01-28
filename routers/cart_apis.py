"""
    @File :   cart_apis.py
    @Author : mukul
    @Date :   27-01-2022
"""
from logger import logging
from service.cart_service import *
from schemas.cart import Cart
from routers.user_apis import verify_token
from fastapi import APIRouter, Depends

route = APIRouter(tags=["CART"])


@route.get("/cart/")
def get_all_item_in_cart(token=Depends(verify_token)):
    """
        desc: created api to get a cart for user.
        param: user_id: it is a user id.
        return: book details from cart in SMD format.
    """
    try:
        user_id = token
        wish_list = retrieve_cart_item(user_id)
        logging.info("Successfully Get All Books From Cart")
        logging.debug(f"Books Details are : {wish_list}")
        return {"status": 200, "message": "Successfully Get Item From Cart Of a User", "data": wish_list}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@route.post("/cart/")
def add_books_to_cart(cart: Cart, token=Depends(verify_token)):
    """
    desc: created api to add book to cart into book store app.
    param1: cart class which contains schema
    return: success message in SMD format
    """
    try:
        user_id = token
        cart_list = add_to_cart(user_id, cart)
        logging.info("Book Successfully Added To Cart")
        return {"status": 200, "message": f"Book Successfully Added To Cart!!", "data": cart_list}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 402, "message": f"Error : {e}"}


@route.delete("/cart/")
def delete_books_from_cart(book_id: int, token=Depends(verify_token)):
    """
    desc: created api to remove book from cart.
    param1: Cart class which contains schema
    return: book_id in SMD format
    """
    try:
        user_id = token
        cart_list = remove_book_from_cart(user_id, book_id)
        logging.info("Book Successfully Removed From Cart")
        return {"status": 200, "message": f"Book Successfully Removed From Cart!!", "data": cart_list}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 402, "message": f"Error : {e}"}


@route.put("/cart/")
def update_books_quantity_cart(cart: Cart, quantity: int, token=Depends(verify_token)):
    """
    desc: created api to remove book from cart.
    param1: Cart class which contains schema
    return: book_id in SMD format
    """
    try:
        user_id = token
        cart_list = update_cart(user_id, quantity, cart)
        logging.info("Cart Successfully Updated")
        return {"status": 200, "message": f"Cart Successfully Updated!!", "data": cart_list}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 402, "message": f"Error : {e}"}
