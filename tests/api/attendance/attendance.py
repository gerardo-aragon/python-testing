from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.attendance.attendance import *
from utils.asserts import *
from pytest_check import check
from utils.preconditions import *


class TestsAttendance:

    def test_01_put_attendance(self,auth):
        attendance = AttendanceApi()

        # Create attendance
        schedule_id, teacher_id, group_id, student_id, start_time, end_time = create_schedule_for_attendance_data(auth)
        attendance.put_create_attendance(auth, 200, schedule_id, teacher_id, group_id,
                                                            student_id, start_time, end_time, "Tardy")


    def test_02_get_attendance(self, auth):
        attendance = AttendanceApi()

        # Get attendance data
        schedule_id, teacher_id, group_id, student_id, start_time, end_time = create_schedule_for_attendance_data(auth)
        attendance_data = attendance.get_attendance_data(auth, 200, student_id, teacher_id, schedule_id)

        # Validate response data
        check.equal(attendance_data[0]["teacherId"], str(teacher_id))
        check.is_true(is_key_present(attendance_data[0], "course"))
        check.is_true(is_key_present(attendance_data[0]["fault"], "type"))


        
        
        



    