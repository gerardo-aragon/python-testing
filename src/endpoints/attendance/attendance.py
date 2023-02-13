from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.groups.groups import *
from utils.payloads.create_attendance import *

@pytest.mark.usefixtures("auth")
class AttendanceApi:

    @staticmethod
    def put_create_attendance(auth, status_code, schedule_id, teacher_id, group_id, student_id, start_time, end_time,
                               attendance_type):
        url = "http://localhost/api/v1/attendance"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        payload = set_create_attendance_payload(schedule_id, teacher_id, group_id, student_id, start_time, end_time,
                                                attendance_type)

        response = put_request(url=url, status_code=status_code, payload=json.dumps(payload), headers=headers)
        return response


    @staticmethod
    def get_attendance_data(auth, status_code, student_id, teacher_id, schedule_id):
        url = f"http://localhost/api/v1/attendance?studentId={student_id}&teacherId={teacher_id}&scheduleId={schedule_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth
        }

        response = get_request(url=url, status_code=status_code, headers=headers)
        return response

        


