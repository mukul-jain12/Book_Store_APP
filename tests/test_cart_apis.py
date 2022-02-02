import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestCase:

    def test_retrieve_cart_detail(self):
        """
        desc: test case for retrieval of all cart item from database.
        """
        response = client.get("/cart/")
        json_response = response.json()
        assert json_response["message"] == "Successfully Get Item From Cart Of a User"

    def test_retrieve_users_detail_if_users_not_exist(self):
        """
        desc: test case for retrieval of a user details from database, but id doesn't exist, so it will raise exception
        """
        response = client.get("/cart/")
        json_response = response.json()
        assert json_response["message"] == "Error : There is no result for the cart."

    @pytest.mark.parametrize('user_data, token_id', [({"book_id": 34}, "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.mUnSxfiXA4zkxTrIVT3l2FRBMfTcHTLOd5oVHDaKnWo")])
    def test_if_book_added_to_wishlist(self, user_data, token_id):
        response = client.post("/cart/", json=user_data, headers={'token': token_id})
        json_response = response.json()
        assert json_response["message"] == "Book Successfully Added To Cart!!"

    @pytest.mark.parametrize('user_data, token_id', [({"book_id": 54}, "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.mUnSxfiXA4zkxTrIVT3l2FRBMfTcHTLOd5oVHDaKnWo")])
    def test_if_book_is_not_added_to_wishlist(self, user_data, token_id):
        response = client.post("/cart/", json=user_data, headers={'token': token_id})
        json_response = response.json()
        assert json_response["message"] != "Book Successfully Added To Cart!!"

    @pytest.mark.parametrize('book_id, token_id', [(34, "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.mUnSxfiXA4zkxTrIVT3l2FRBMfTcHTLOd5oVHDaKnWo")])
    def test_if_book_is_removed_from_wishlist(self, book_id, token_id):
        response = client.delete(f"/cart/{book_id}", headers={'token': token_id})
        json_response = response.json()
        assert json_response["message"] == "Successfully Deleted The User Details"

    @pytest.mark.parametrize('book_id, token_id', [(44, "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.mUnSxfiXA4zkxTrIVT3l2FRBMfTcHTLOd5oVHDaKnWo")])
    def test_if_book_is_not_removed_from_wishlist(self, book_id, token_id):
        response = client.delete(f"/cart/{book_id}", headers={'token': token_id})
        json_response = response.json()
        assert json_response["message"] == "Error : There is no result for these book in the cart."

    @pytest.mark.parametrize('book_id, quantity, token_id', [(6, 5, "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.mUnSxfiXA4zkxTrIVT3l2FRBMfTcHTLOd5oVHDaKnWo")])
    def test_if_book_is_updated_in_wishlist(self, book_id, quantity, token_id):
        response = client.put(f"/cart/{book_id}/{quantity}", headers={'token': token_id})
        json_response = response.json()
        assert json_response["message"] == "Cart Successfully Updated!!"

    @pytest.mark.parametrize('book_id, quantity, token_id', [(54, 5, "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.mUnSxfiXA4zkxTrIVT3l2FRBMfTcHTLOd5oVHDaKnWo")])
    def test_if_book_is_not_updated_in_wishlist(self, book_id, quantity, token_id):
        response = client.put(f"/cart/{book_id}/{quantity}", headers={'token': token_id})
        json_response = response.json()
        assert json_response["message"] == "Error : There is no result for these book in the cart."
