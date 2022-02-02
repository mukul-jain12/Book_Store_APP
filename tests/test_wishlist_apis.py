import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestCase:

    @pytest.mark.parametrize('token_id', ["eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.mUnSxfiXA4zkxTrIVT3l2FRBMfTcHTLOd5oVHDaKnWo"])
    def test_retrieve_wishlist_for_a_user(self, token_id):
        """
            desc: test case for retrieval of all books in wishlist for a users.
        """
        response = client.get("/wishlist/", headers={'token': token_id})
        json_response = response.json()
        assert json_response["message"] == "Successfully Get A Wishlist"

    @pytest.mark.parametrize('token_id', ["eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1fQ.K4UUqOCE7e7M4yo9LTs2gUaJURg-8DAajx95oj-QIgQ"])
    def test_retrieve_users_detail_if_users_not_exist(self, token_id):
        """
            desc: test case for retrieval of all books from wishlist for a user from database, but id doesn't exist, so it will raise exception
        """
        response = client.get("/wishlist/", headers={'token': token_id})
        json_response = response.json()
        assert json_response["message"] == "Error : There is no result for the Wishlist."

    @pytest.mark.parametrize('user_data, token_id', [({"book_id": 17}, "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.mUnSxfiXA4zkxTrIVT3l2FRBMfTcHTLOd5oVHDaKnWo")])
    def test_if_user_added_to_db(self, user_data, token_id):
        response = client.post("/wishlist/", json=user_data, headers={'token': token_id})
        assert response.json()["message"] == "Book Successfully Added To wishlist!!"

    @pytest.mark.parametrize('book_id, token_id', [(7, "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.mUnSxfiXA4zkxTrIVT3l2FRBMfTcHTLOd5oVHDaKnWo")])
    def test_if_user_is_deleted(self, book_id, token_id):
        response = client.delete(f"/wishlist/{book_id}", headers={'token': token_id})
        json_response = response.json()
        assert json_response["message"] != "Book Successfully Removed From wishlist!!"
