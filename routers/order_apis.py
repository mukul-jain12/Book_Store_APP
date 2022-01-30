"""
    @File :   order_apis.py
    @Author : mukul
    @Date :   29-01-2022
"""

from logger import logging
from service.order_service import *
from schemas.order import Order
from routers.user_apis import verify_token
from fastapi import APIRouter, Depends

route = APIRouter(tags=["CART"])


@route.post("/order/")
def place_order(order: Order, token=Depends(verify_token)):
    """
    desc: created api to order the book from book store app.
    param1: order class which contains schema
    return: success message in SMD format
    """
    try:
        user_id = token
        cart_list = book_order(user_id, order)
        logging.info("Book Successfully Ordered")
        return {"status": 200, "message": f"Book Successfully Ordered!!", "data": cart_list}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 402, "message": f"Error : {e}"}
