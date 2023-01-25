import json
import pytest
from utils.api_helper import *
from utils.payloads.create_course import *


@pytest.mark.usefixtures("auth")
class CoursesApi:

    @staticmethod
    def post_create_courses(auth, status_code, course_name):
        url = "http://localhost/api/v1/courses"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = set_create_course_payload(course_name)

        response = post_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response


    @staticmethod
    def get_all_courses(auth, status_code):
        url = "http://localhost/api/v1/courses"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_all_courses_view(auth, status_code):
        url = "http://localhost/api/v1/courses/view"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_course_by_id(auth, status_code, course_id):
        url = f"http://localhost/api/v1/courses/{course_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def put_edit_course(auth, status_code, course_id):
        url = f"http://localhost/api/v1/courses/{course_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = set_edit_course_payload()

        response = put_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response