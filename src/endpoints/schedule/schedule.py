import json
import pytest
from utils.api_helper import *
from utils.payloads.create_schedule import *


@pytest.mark.usefixtures("auth")
class ScheduleApi:

    @staticmethod
    def post_create_schedule(auth, status_code, schedule_name, group_id):
        url = "http://localhost/api/v1/schedule"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = set_create_schedule_payload(schedule_name, group_id)

        response = post_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response
    
    
    @staticmethod
    def delete_schedule(auth, status_code, schedule_id):
        url = f"http://localhost/api/v1/schedules/{schedule_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = delete_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_all_schedule_by_group_id(auth, status_code, group_id):
        url = f"http://localhost/api/v1/schedules/{group_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_schedule_by_id(auth, status_code, schedule_id):
        url = f"http://localhost/api/v1/schedule/{schedule_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def put_edit_schedule(auth, status_code, schedule_id, group_id, schedule_name):
        url = f"http://localhost/api/v1/schedules"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = set_edit_schedule_payload(schedule_id, group_id, schedule_name)

        response = put_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response