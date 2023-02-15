import json
import time

from src.endpoints.alerts.alerts import *
from src.endpoints.faults.faults import *
from src.endpoints.groups.groups import *
from src.endpoints.schedule.schedule import *
from src.endpoints.student.student import *
from src.endpoints.attendance.attendance import *
from datetime import datetime

def create_random_fields():
    time.sleep(1)
    epoch = datetime.today().strftime('%s')
    field_name = epoch
    return field_name

def create_parametrize_data():
    cedula_id = create_random_fields()
    email = create_random_fields() + "@gmail.com"
    user_name = create_random_fields()
    return cedula_id, email, user_name


def create_fault(auth):
    schedule = ScheduleApi()
    faults = FaultsApi()
    group = GroupsApi()
    student = StudentApi()

    # Search an existent group (Created previously by database)
    search_group = group.get_search_group(auth, 200, "7-1 (No eliminar)")
    group_id = search_group["data"][0]["id"]

    # Create schedule
    schedule_name = "Horario " + create_random_fields()
    dictionary = schedule.post_create_schedule(auth, 201, schedule_name, group_id)

    # Get student
    student_id = student.get_students_by_group(auth, 200, "7-1 (No eliminar)")
    response_body = \
        faults.post_create_faults(auth, 201, group_id, student_id['data'][0]['cedulaId'], "Tardy", dictionary["id"])
    return response_body


def create_schedule_for_attendance_data(auth):
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


def get_student_data(auth):
    schedule = ScheduleApi()
    group = GroupsApi()
    student = StudentApi()

    # Search an existent group (Created previously by database)
    search_group = group.get_search_group(auth, 200, "7-1 (No eliminar)")
    group_id = search_group["data"][0]["id"]

    # Create schedule
    schedule_name = "Horario " + (create_random_fields()[-5:])
    schedule_data = schedule.post_create_schedule(auth, 201, schedule_name, group_id)
    schedule_id = schedule_data["id"]

    # Get student
    student_data = student.get_students_by_group(auth, 200, "7-1 (No eliminar)")
    return group_id, schedule_id, student_data