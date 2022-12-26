import json
import pytest
from utils.api_helper import *
from utils.payloads.create_administrator import *

@pytest.mark.usefixtures("auth")
class AdministratorApi:


    @staticmethod
    def post_create_administrator(auth, status_code):
        url = "http://localhost/api/v1/users/admins"

        payload = json.dumps(payload_create_admin)
    
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = post_request(url=url, status_code=status_code, payload=payload, headers=headers)
        return response


    @staticmethod
    def get_users(auth, status_code):
        url = "http://localhost/api/v1/users?page=1&take=10&role=ADMIN&search="

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response

