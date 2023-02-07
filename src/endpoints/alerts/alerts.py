import json
import pytest
from utils.api_helper import *


@pytest.mark.usefixtures("auth")
class AlertsApi:

    @staticmethod
    def post_create_notes(auth, status_code, student_id, user_id, message):
        url = "http://localhost/api/v1/alerts/students/notes"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = {
            "studentId": student_id,
            "userId": user_id,
            "message": message
        }

        response = post_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response


    @staticmethod
    def get_student_alert_notes(auth, status_code, student_id):
        url = f"http://localhost/api/v1/alerts/students/{student_id}/notes"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response


    @staticmethod
    def get_student_alert_notes_pdf(auth, status_code, student_id):
        url = f"http://localhost/api/v1/alerts/students/{student_id}/pdf"

        headers = {
            'Content-Type': 'application/pdf',
            'ETag': 'W/"11a93-kqb7mHvadygPKyx+aqExuSm5Wjg"',
            'Connection': 'keep-alive',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request_pdf(url=url, status_code=status_code, headers=headers)
        return response