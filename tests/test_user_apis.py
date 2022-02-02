import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestCase:

    def test_retrieve_users_detail(self):
        """
        desc: test case for retrieval of all users from database.
        """
        response = client.get("/users/")
        json_response = response.json()
        assert json_response["message"] == "Successfully Get All User Details"

    def test_retrieve_users_detail_if_users_not_exist(self):
        """
        desc: test case for retrieval of a user details from database, but id doesn't exist, so it will raise exception
        """
        response = client.get(f"/users/")
        json_response = response.json()
        assert json_response["message"] == "Error : There is no result for the user data."

    @pytest.mark.parametrize('user_id', [3, 4, 5])
    def test_retrieve_user_detail(self, user_id):
        """
            desc: test case for retrieval of an employee from database.
            param: user_id: it is a user id
        """
        response = client.get(f"/user/?user_id={user_id}")
        json_response = response.json()
        assert json_response["message"] == "Successfully Get A User Details"

    @pytest.mark.parametrize('user_id', [13, 14, 15])
    def test_retrieve_user_detail_if_user_not_exist(self, user_id):
        """
        desc: test case for retrieval of a user details from database, but id doesn't exist, so it will raise exception
        """
        response = client.get(f"/user/?user_id={user_id}")
        json_response = response.json()
        assert json_response["message"] == "Error : User with this Id doesn't exist in the Database!"

    @pytest.mark.parametrize('user_data', [{"user_name": "ramuesh", "password": "1k23", "email_id": "abcd@gmail.com", "mobile_number": 79357393}])
    def test_if_user_added_to_db(self, user_data):
        response = client.post("/user/registration/", json=user_data)
        assert response.json()["message"] == "Successfully Registered The User!!"

    @pytest.mark.parametrize('user_data', [{"user_name": "string", "password": "string", "email_id": "mukuljain422@gmail.com", "mobile_number": 0}])
    def test_if_user_is_not_added_to_db(self, user_data):
        response = client.post("/user/registration/", json=user_data)
        assert response.status_code == 200
        assert response.json()["message"] != "Successfully Registered The User!!"

    @pytest.mark.parametrize('email_id , password', [('mukuljain422@gmail.com', 'string'), ('kavyajain730@gmail.com', 'string'), ('dibyeshmishra207@gmail.com', 'string')])
    def test_user_login_is_successful(self, email_id, password):
        response = client.post(f"/user/login/?email_id={email_id}&password={password}")
        json_response = response.json()
        assert json_response["message"] == "Successfully Logged In and Generated the token"

    @pytest.mark.parametrize('email_id , password', [('mukuljain422@gmail.com', 'mukul@1234'), ('kavyajain7@gmail.com', 'string'), ('dibyeshmishra207@gmail.com', 'dibyesh')])
    def test_user_login_is_not_successful(self, email_id, password):
        response = client.post(f"/user/login/?email_id={email_id}&password={password}")
        json_response = response.json()
        assert json_response["message"] == "Error : Credentials Are incorrect, Please Try again!"

    @pytest.mark.parametrize('token_id', ["eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbF9pZCI6ImRpYnllc2htaXNocmEyMDdAZ21haWwuY29tIn0.pId3nRuXCAWD77FcrtwoDGOVaCaTCKD5s-aXUKLebM4"])
    def test_user_is_verified(self, token_id):
        response = client.get(f"/user/verification/{token_id}", headers={"token": token_id})
        json_response = response.json()
        assert json_response["message"] == "Successfully Done User Verification!!"

    @pytest.mark.parametrize('token_id', ["eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbF9pZCI6Im11a3VsamFpbjQyMkBnbWFpbC5jb20ifQ.JZMt795SCpO87humk0ZvglP2vqsGxYBdAHplmgyvY6A"])
    def test_user_is_not_verified(self, token_id):
        response = client.get(f"/user/verification/{token_id}", headers={"token": token_id})
        json_response = response.json()
        assert json_response["message"] == "Error: User with this Id already verified!"

    @pytest.mark.parametrize('user_id', [4])
    def test_if_user_is_deleted(self, user_id):
        response = client.delete(f"/user/{user_id}")
        json_response = response.json()
        assert json_response["message"] == "Successfully Deleted The User Details"

    @pytest.mark.parametrize('user_id', [6, 8, 10])
    def test_if_user_is_not_deleted(self, user_id):
        response = client.delete(f"/user/{user_id}")
        json_response = response.json()
        assert json_response["message"] == "Error : User with this Id doesn't exist in the Database!"

    @pytest.mark.parametrize('user_id, user_data', [(3, {"user_name": "string", "password": "string", "email_id": "mukuljain578@gmail.com", "mobile_number": 78357393})])
    def test_if_user_updated_to_db(self, user_id, user_data):
        response = client.put(f"/user/{user_id}", json=user_data)
        json_response = response.json()
        assert json_response["message"] == "Successfully Updated The User Details"

    @pytest.mark.parametrize('user_id, user_data', [(9, {"user_name": "shivam", "password": "123", "email_id": "shivammishra@gmail.com", "mobile_number": 78357393})])
    def test_if_user_details_not_updated_to_db(self, user_id, user_data):
        response = client.put(f"/user/{user_id}", json=user_data)
        json_response = response.json()
        assert json_response["message"] == "Error : User with this Id doesn't exist in the Database!"
