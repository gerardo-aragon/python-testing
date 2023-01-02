import json
import pytest
from utils.api_helper import *
@pytest.mark.usefixtures("auth")
class UsersApi:

    @staticmethod
    def get_user(auth, status_code, user_id):
        
        url = f"http://localhost/api/v1/users/{user_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response