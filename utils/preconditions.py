import json
import datetime
import time

from src.endpoints.alerts.alerts import *
from src.endpoints.faults.faults import *
from src.endpoints.groups.groups import *
from src.endpoints.schedule.schedule import *
from src.endpoints.student.student import *

def create_random_fields():
    time.sleep(1)
    epoch = datetime.datetime.today().strftime('%s')
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