import json
import pytest
from utils.api_helper import *
from utils.payloads.create_teacher import *

@pytest.mark.usefixtures("auth")
class TeacherApi:


    @staticmethod
    def post_create_teacher(auth, status_code, cedula_id, email, user_name):
        url = "http://localhost/api/v1/users/teachers"
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = set_create_teacher_payload(cedula_id, email, user_name)

        response = post_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response

    @staticmethod
    def put_edit_teacher(auth, status_code, admin_id, email, user_name):
        url = f"http://localhost/api/v1/users/{admin_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = set_edit_teacher_payload(email, user_name)

        response = put_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response


    @staticmethod
    def get_teacher_users(auth, status_code):
        url = "http://localhost/api/v1/users?page=1&take=10&role=TEACHER&search="

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def delete_teacher_user(auth, status_code, admin_id):
        url = f"http://localhost/api/v1/users/{admin_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = delete_request(url=url, status_code=status_code, headers=headers)
        return response

