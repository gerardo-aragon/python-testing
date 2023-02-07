import json
import pytest
from utils.api_helper import *
from utils.payloads.create_student import *

@pytest.mark.usefixtures("auth")
class StudentApi:


    @staticmethod
    def post_create_student(auth, status_code, cedula_id):
        url = "http://localhost/api/v1/students"
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = set_create_student_payload(cedula_id)

        response = post_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response

    @staticmethod
    def put_edit_student(auth, status_code, student_id):
        url = f"http://localhost/api/v1/students"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = set_edit_student_payload(student_id)

        response = put_request(url=url, payload=json.dumps(payload), status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_student_users(auth, status_code):
        url = "http://localhost/api/v1/students"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def delete_student_user(auth, status_code, student_id):
        url = f"http://localhost/api/v1/students/{student_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = delete_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_specific_student_user(auth, status_code, student_id):
        url = f"http://localhost/api/v1/students/{student_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_students_by_group(auth, status_code, group_name):
        url = f"http://localhost/api/v1/students?page=1&search={group_name}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response




