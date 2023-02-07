import pytest
import requests
import json


def get_request(url, status_code, headers=None, params=None):
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == status_code
    response_data = json.loads(str(response.text))
    return response_data


def post_request(url, payload, status_code, headers=None, params=None):
    response = requests.post(url, payload, headers=headers, params=params)
    assert response.status_code == status_code
    response_data = json.loads(str(response.text))
    return response_data


def put_request(url, payload, status_code, headers=None, params=None):
    response = requests.put(url, payload, headers=headers, params=params)
    assert response.status_code == status_code
    response_data = json.loads(str(response.text))
    return response_data


def delete_request(url, status_code, headers=None, params=None):
    response = requests.delete(url, headers=headers, params=params)
    assert response.status_code == status_code
    response_data = json.loads(str(response.text))
    return response_data


def get_request_pdf(url, status_code, headers=None, params=None):
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == status_code
    response_data = response.text
    return response_data