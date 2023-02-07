import json
import time

from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.alerts.alerts import *
from src.endpoints.faults.faults import *
from src.endpoints.groups.groups import *
from src.endpoints.schedule.schedule import *
from src.endpoints.student.student import *
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

def create_fault(auth):
    schedule = ScheduleApi()
    faults = FaultsApi()
    group = GroupsApi()
    student = StudentApi()

    # Search an existent group (Created previously by database)
    search_group = group.get_search_group(auth, 200, "7-1 (No eliminar)")
    group_id = search_group["data"][0]["id"]

    # Create schedule
    schedule_name = create_parametrize_data()
    dictionary = schedule.post_create_schedule(auth, 201, schedule_name, group_id)

    # Get student
    student_id = student.get_students_by_group(auth, 200, "7-1 (No eliminar)")
    response_body = \
        faults.post_create_faults(auth, 201, group_id, student_id['data'][0]['cedulaId'], "Tardy", dictionary["id"])
    return response_body
    

@pytest.mark.usefixtures("auth")
class TestAlertsApi:

    def test_01_create_fault_notes(self, auth):
        alerts = AlertsApi()

        # Create fault
        fault_data = create_fault(auth)
        student_id = fault_data[0]['studentId']
        user_id = fault_data[0]['userId']
        
        # Create note
        note_data = alerts.post_create_notes(auth, 201, student_id, user_id, "Note 0001")

        # Validate the data in the response
        check.equal(note_data["studentId"], student_id)
        check.equal(note_data["userId"], user_id)


    def test_02_get_student_alerts_notes(self, auth):
        alerts = AlertsApi()

        # Create fault and note
        fault_data = create_fault(auth)
        student_id = fault_data[0]['studentId']
        user_id = fault_data[0]['userId']
        alerts.post_create_notes(auth, 201, student_id, user_id, "Note 0001")

        # Get notes by student
        notes_data = alerts.get_student_alert_notes(auth, 200, student_id)

        # Validate the data in the response
        check.equal(notes_data[0]["message"], "Note 0001")
        check.is_true(is_key_present(notes_data[0], "userName"))
        check.is_true(is_key_present(notes_data[0], "userLastName"))


    def test_03_get_student_alerts_notes_pdf(self, auth):
        alerts = AlertsApi()

        # Create fault and note
        fault_data = create_fault(auth)
        student_id = fault_data[0]['studentId']
        user_id = fault_data[0]['userId']
        alerts.post_create_notes(auth, 201, student_id, user_id, "Note 0001")

        # Get notes by student
        alerts.get_student_alert_notes_pdf(auth, 200, student_id)




        
        