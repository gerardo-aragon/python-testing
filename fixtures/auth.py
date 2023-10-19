import pytest
import json

import requests
from utils.api_helper import *


@pytest.fixture(name="auth", scope="function", autouse=True)
def auth(request):
    url = "http://localhost:80/api/v1/authenticate"
    payload = json.dumps({
        "userName": "gerardo.aragon",
        "password":  request.config.getoption("--password")
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = post_request(url=url, payload=payload, status_code=201, headers=headers)
    return response['accessToken']
