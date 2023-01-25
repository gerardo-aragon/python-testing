import datetime
import time


def set_create_course_payload(course_name):
    payload_create_course = [{
        "name": course_name,
        "teachers": [
            "luis.ponce"
        ]
    }]
    return payload_create_course


def set_edit_course_payload():
    payload_edit_course = {
        "name": "Español",
        "teacherIds": [
            208340998
        ]
    }
    return payload_edit_course