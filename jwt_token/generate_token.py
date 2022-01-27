"""
    @File :   generate_token.py
    @Author : mukul
    @Date :   20-01-2022
"""
import jwt


def encode_register_token(user_email):
    """
        desc: this function will encode the payload into a token
        param: user_email: it is an user email
        return: generated token id for email
    """
    payload = {"email_id": user_email}
    token_id = jwt.encode(payload, "secret")
    return token_id


def decode_register_token(user_token):
    """
        desc: this function will decode the token into a payload
        param: token_id: it is a token which generated at the time of registration
        return: decoded user email
    """
    payload = jwt.decode(user_token, "secret", algorithms=["HS256"])
    return payload.get('email_id')


def encode_login_token(user_id):
    """
        desc: this function will encode the payload into a token
        param: user_id: it is an user id
        return: generated token id
    """
    payload = {"user_id": user_id}
    token_id = jwt.encode(payload, "secret")
    return token_id


def decode_login_token(user_token):
    """
        desc: this function will decode the payload into a token
        param: user_token: it is a login token for user
        return: decoded user_id
    """
    payload = jwt.decode(user_token, "secret", algorithms=["HS256"])
    return payload.get('user_id')
