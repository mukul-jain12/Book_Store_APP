import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestCase:

    def test_retrieve_books(self):
        """
        desc: test case for retrieval of all books from database.
        """
        response = client.get("/books/")
        json_response = response.json()
        assert json_response["message"] == "Successfully Get All Books Details"

    def test_books_not_retrieved(self):
        """
        desc: test case for retrieval of all books from database, but id doesn't exist, so it will raise exception
        """
        response = client.get("/books/")
        json_response = response.json()
        assert json_response["message"] == "Error : There is no result for the book."

    @pytest.mark.parametrize('user_data', [{"author_name": "Mukul Jain", "title": "Rasta", "image": "jkascn", "quantity": 20, "price": 300, "description": "Padhai kar Lo bss"}])
    def test_if_book_is_not_added(self, user_data):
        response = client.post("/book/", json=user_data)
        json_response = response.json()
        assert json_response["message"] == "Successfully Added The Book!!"

    @pytest.mark.parametrize('book_id', [50])
    def test_if_book_is_removed_from_books(self, book_id):
        response = client.delete(f"/book/{book_id}")
        json_response = response.json()
        assert json_response["message"] == "Successfully Deleted The Book Details"

    @pytest.mark.parametrize('book_id', [50])
    def test_if_book_is_not_removed_from_books(self, book_id):
        response = client.delete(f"/book/{book_id}")
        json_response = response.json()
        assert json_response["message"] == "Error : Book with this Id doesn't exist in the Database!"

    @pytest.mark.parametrize('book_id, book_data', [(2, {'author_name': "Mukul Jain", "title": "Indian Superfoods", "image": "http://books.google.com/books/content?id=4oFoDwAAQBAJ&printsec=frontcover&img=1&zoom=5", "quantity": 12, "price": 495, "description": "Forget about acacia seeds and goji berries. The secret foods for healthvitality and weight loss lie in our own kitchens and backyards. Top nutritionist Rujuta Diwekar talks you through the ten Indian superfoods that will completely transform you"})])
    def test_if_book_is_updated_in_wishlist(self, book_id, book_data):
        response = client.put(f"/book/{book_id}", json=book_data)
        json_response = response.json()
        assert json_response["message"] == "Successfully Updated The Book Details"

    @pytest.mark.parametrize('book_id, book_data', [(58, {'author_name': "Rujuta Divekar", "title": "Indian Superfoods", "image": "http://books.google.com/books/content?id=4oFoDwAAQBAJ&printsec=frontcover&img=1&zoom=5", "quantity": 12, "price": 495, "description": "Forget about acacia seeds and goji berries. The secret foods for healthvitality and weight loss lie in our own kitchens and backyards. Top nutritionist Rujuta Diwekar talks you through the ten Indian superfoods that will completely transform you"})])
    def test_if_book_is_not_updated_in_wishlist(self, book_id, book_data):
        response = client.put(f"/book/{book_id}", json=book_data)
        json_response = response.json()
        assert json_response["message"] == "Error : Book with this Id doesn't exist in the Database!"
