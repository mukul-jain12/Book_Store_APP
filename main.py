"""
    @File :   main.py
    @Author : mukul
    @Date :   20-01-2022
"""
import uvicorn
from fastapi import FastAPI, Header
from logger import logging
from jwt_token.generate_token import *
from service.user_service import *
from schemas.users import Users

app = FastAPI(title="Book Store App")


@app.get("/users/", tags=["USERS"])
def get_all_users_details():
    """
        desc: created api to get all the users details.
        return: user details in SMD format.
        """
    try:
        user_details = retrieve_all_users()
        logging.info("Successfully Get All User Details")
        logging.debug(f"User Details are : {user_details}")
        return {"status": 200, "message": "Successfully Get All User Details", "data": user_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@app.get("/user/", tags=["USERS"])
def get_user_details(user_id: int):
    """
        desc: created api to get a user details.
        param: user_id: it is a user id.
        return: user details in SMD format.
        """
    try:
        user_details = retrieve_user(user_id)
        logging.info("Successfully Get A User Detail")
        logging.debug(f"User Details are : {user_details}")
        return {"status": 200, "message": "Successfully Get A User Details", "data": user_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@app.post("/user/registration/", tags=["USERS"])
def user_registration(users: Users):
    """
    desc: created api to register the user into book store app.
    param1: Users class which contains schema
    return: user_token in SMD format
    """
    try:
        user_details = register_user(users)
        logging.info("User Successfully Registered")
        logging.debug(f"User Details are : {user_details}")
        user_token = encode_register_token(user_details.email_id)
        return {"status": 200, "message": "Successfully Registered The User", "token": user_token}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 402, "message": "Error : Employee with this Id Already exist in database"}


@app.post("/user/verification/{user_token}", tags=["USERS"])
def user_verification(token: str = Header(None)):
    """
        desc: user verification by entering the token number generated at registration
        param: token: encoded user email id
    """
    try:
        token_id = decode_register_token(token)
        check_user = retrieve_user_by_email_id(token_id)
        verify_user = verification(check_user[0]["is_verified"], token_id)
        return {"status": 200, "message": "Successfully Done User Verification!!", "data": verify_user}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 401, "message": f"{e}"}


@app.delete("/user/", tags=["USERS"])
def delete_user_details(user_id: int):
    """
    desc: created api to delete the user details using user id
    param: user_id: it is a user id
    return: u_id in SMD format
    """
    try:
        retrieve_user(user_id)
        u_id = delete_user(user_id)
        logging.info("Successfully Deleted The User Details")
        logging.debug(f"User ID is : {u_id}")
        return {"status": 204, "message": "Successfully Deleted The User Details", "data": u_id}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@app.put("/user/", tags=["USERS"])
def update_user_details(user_id: int, users: Users):
    """
    desc: created api to update any item in the database table
    param1: user_id: it is a user id
    param2: Users class which contains schema
    return: user details in SMD format
    """
    try:
        retrieve_user(user_id)
        user_details = update_user(user_id, users)
        logging.info("Successfully Updated The User Details")
        logging.debug(f"User Details are : {user_details}")
        return {"status": 200, "message": "Successfully Updated The User Details", "data": user_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.post("/user/login/", tags=["USERS"])
def user_login(email_id: str, password: str):
    """
    desc: created api to login into boost store app
    param1: id: it is a user email id
    param2: password: user password
    return: user details in SMD format
    """
    try:
        user_details = login_into_book_store(email_id, password)
        logging.info("Successfully Login into Book Store App!!")
        logging.debug(f"User Details are : {user_details}")
        user_token = encode_login_token(user_details[0]["id"])
        return {"status": 200, "message": "Successfully Generated the token", "token": user_token, "data": user_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 401, "message": f"Error : {e}"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
