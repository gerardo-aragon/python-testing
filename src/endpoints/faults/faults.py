import json
import pytest
from utils.api_helper import *
from utils.payloads.create_fault import *
from datetime import datetime, timedelta

@pytest.mark.usefixtures("auth")
class FaultsApi:

    @staticmethod
    def get_student_faults(auth, status_code):
        url = "http://localhost/api/v1/students/faults"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response

    @staticmethod
    def post_create_faults(auth, status_code, group_id, student_id, fault_type, schedule_id):
        url = f"http://localhost/api/v1/faults/{schedule_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = set_create_fault_payload(group_id, student_id, fault_type)

        response = post_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response

    @staticmethod
    def post_create_student_faults(auth, status_code, group_id, student_id, fault_type, schedule_id):
        url = f"http://localhost/api/v1/faults/students/{schedule_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = [set_create_fault_payload(group_id, student_id, fault_type)]

        response = post_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response



    @staticmethod
    def get_faults_student_count(auth, status_code):
        url = "http://localhost/api/v1/faults/student-count"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def put_justify_absence(auth, status_code, absence_id):
        url = f"http://localhost/api/v1/faults/{absence_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = put_justify_fault_payload()

        response = put_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response




