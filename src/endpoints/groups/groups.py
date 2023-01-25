import json
import pytest
from utils.api_helper import *
from utils.payloads.create_groups import *


@pytest.mark.usefixtures("auth")
class GroupsApi:

    @staticmethod
    def post_create_groups(auth, status_code, group_name):
        url = "http://localhost/api/v1/groups"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = set_create_group_payload(group_name)

        response = post_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response


    @staticmethod
    def delete_group(auth, status_code, group_id):
        url = f"http://localhost/api/v1/groups/{group_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = delete_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_all_groups(auth, status_code):
        url = "http://localhost/api/v1/groups"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_groups_by_user_role(auth, status_code, user_name, role):
        url = f"http://localhost/api/v1/groups/{user_name}&{role}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_group_classes_by_username(auth, status_code, user_name):
        url = f"http://localhost/api/v1/groups/classes/{user_name}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_students_by_group(auth, status_code, group_id):
        url = f"http://localhost/api/v1/groups/{group_id}/students"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_search_group(auth, status_code, group_name):
        url = f"http://localhost/api/v1/groups/?search={group_name}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_group_faults(auth, status_code, group_id):
        url = f"http://localhost/api/v1/groups/{group_id}/faults"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_group_by_id(auth, status_code, group_id):
        url = f"http://localhost/api/v1/groups/{group_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def put_edit_group(auth, status_code, group_id, group_name):
        url = f"http://localhost/api/v1/groups/{group_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = set_edit_group_payload(group_name)

        response = put_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response




