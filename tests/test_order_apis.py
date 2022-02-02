import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestCase:

    @pytest.mark.parametrize('token_id', ["eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.mUnSxfiXA4zkxTrIVT3l2FRBMfTcHTLOd5oVHDaKnWo"])
    def test_order_retrieved(self, token_id):
        """
        desc: test case for retrieval of all orders from database, but id doesn't exist, so it will raise exception
        """
        response = client.get("/order/", headers={'token': token_id})
        json_response = response.json()
        assert json_response["message"] == "Successfully Get All Order."

    @pytest.mark.parametrize('token_id', ["eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1fQ.K4UUqOCE7e7M4yo9LTs2gUaJURg-8DAajx95oj-QIgQ"])
    def test_retrieve_order(self, token_id):
        """
        desc: test case for retrieval of all orders for user.
        """
        response = client.get("/order/", headers={'token': token_id})
        json_response = response.json()
        assert json_response["message"] == "Error : User not ordered any book from the book."

    @pytest.mark.parametrize('order_data, token_id', [({"address": 'Dungarpur'},"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.mUnSxfiXA4zkxTrIVT3l2FRBMfTcHTLOd5oVHDaKnWo")])
    def test_for_order_is_placed_for_user(self, order_data, token_id):
        response = client.post("/order/", json=order_data, headers={"token": token_id})
        json_response = response.json()
        assert json_response["message"] == "Book Successfully Ordered!!"

    @pytest.mark.parametrize('order_data, token_id', [({"address": 'Dungarpur'}, "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.mUnSxfiXA4zkxTrIVT3l2FRBMfTcHTLOd5oVHDaKnW")])
    def test_for_order_is_placed_for_user(self, order_data, token_id):
        response = client.post("/order/", json=order_data, headers={"token": token_id})
        json_response = response.json()
        assert json_response["detail"] == "You are not a authorized person"
