from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.groups.groups import *
from src.endpoints.schedule.schedule import *
from src.endpoints.student.student import *
from src.endpoints.attendance.attendance import *
from utils.asserts import *
from pytest_check import check


def create_random_field():
    time.sleep(1)
    epoch = datetime.datetime.today().strftime('%s')
    schedule_name = epoch
    return schedule_name[-5:]


def create_parametrize_data():
    schedule_name = "Horario " + create_random_field()
    return schedule_name


def schedule_preconditions(auth):
    schedule = ScheduleApi()
    group = GroupsApi()
    student = StudentApi()
    attendance = AttendanceApi()

    # Get student in the group
    student_data = student.get_students_by_group(auth, 200, "7-1 (No eliminar)")
    student_id = student_data['data'][0]['cedulaId']

    # Get teacher and schedules in the group
    search_group = group.get_search_group(auth, 200, "7-1 (No eliminar)")
    group_id = search_group["data"][0]["id"]
    teacher_id = search_group['data'][0]['managerId']
    schedules_data = schedule.get_all_schedule_by_group_id(auth, 200, group_id)
    schedule_id = schedules_data[0]['id']

    # Get attendance data
    attendance_data = attendance.get_attendance_data(auth, 200, student_id, teacher_id, schedule_id)
    start_time = attendance_data[0]['start']
    end_time = attendance_data[0]['end']
    
    return schedule_id, teacher_id, group_id, student_id, start_time, end_time
    

class TestsAttendance:

    def test_01_put_attendance(self,auth):
        attendance = AttendanceApi()

        # Create attendance
        schedule_id, teacher_id, group_id, student_id, start_time, end_time = schedule_preconditions(auth)
        attendance.put_create_attendance(auth, 200, schedule_id, teacher_id, group_id,
                                                            student_id, start_time, end_time, "Tardy")


    def test_02_get_attendance(self, auth):
        attendance = AttendanceApi()

        # Get attendance data
        schedule_id, teacher_id, group_id, student_id, start_time, end_time = schedule_preconditions(auth)
        attendance_data = attendance.get_attendance_data(auth, 200, student_id, teacher_id, schedule_id)

        # Validate response data
        check.equal(attendance_data[0]["teacherId"], str(teacher_id))
        check.is_true(is_key_present(attendance_data[0], "course"))
        check.is_true(is_key_present(attendance_data[0]["fault"], "type"))


        
        
        



    