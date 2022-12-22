import json
import pytest
from utils.api_helper import *


@pytest.mark.usefixtures("auth")
class AuthenticationApi:


    @staticmethod
    def authenticate(username, password, status_code):
        url = "http://localhost:80/api/v1/authenticate"
        payload = json.dumps({
            "userName": username,
            "password": password
        })

        headers = {
            'Content-Type': 'application/json',
        }

        response = post_request(url=url, status_code=status_code, payload=payload, headers=headers)
        return response