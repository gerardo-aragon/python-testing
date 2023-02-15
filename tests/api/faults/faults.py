import json
import time

from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.faults.faults import *
from src.endpoints.schedule.schedule import *
from utils.asserts import *
from pytest_check import check
from utils.preconditions import *


@pytest.mark.usefixtures("auth")
class TestAlertsApi:

    def test_01_create_fault_by_schedule_tardy(self, auth):
        faults = FaultsApi()
        schedule = ScheduleApi()

        group_id, schedule_id, student_id = get_student_data(auth)

        # Create fault
        fault_data = faults.post_create_faults(auth, 201, group_id, student_id['data'][0]['cedulaId'], "Tardy", schedule_id)

        # Validate response body
        check.is_true(is_key_present(fault_data[0], "status"))
        check.equal(fault_data[0]["groupId"], group_id)
        check.equal(fault_data[0]["type"], "Tardy")

        # Delete schedule
        schedule.delete_schedule(auth, 200, schedule_id)


    def test_02_create_fault_by_schedule_absence(self, auth):
        faults = FaultsApi()
        schedule = ScheduleApi()

        group_id, schedule_id, student_id = get_student_data(auth)

        # Create fault
        fault_data = faults.post_create_faults(auth, 201, group_id, student_id['data'][1]['cedulaId'], "Absence", schedule_id)

        # Validate response body
        check.is_true(is_key_present(fault_data[0], "status"))
        check.equal(fault_data[0]["groupId"], group_id)
        check.equal(fault_data[0]["type"], "Absence")

        # Delete schedule
        schedule.delete_schedule(auth, 200, schedule_id)


    def test_03_create_students_fault_tardy(self, auth):
        faults = FaultsApi()
        schedule = ScheduleApi()

        group_id, schedule_id, student_id = get_student_data(auth)

        # Create fault
        fault_data = faults.post_create_student_faults(auth, 201, group_id, student_id['data'][2]['cedulaId'], "Tardy", schedule_id)

        # Validate response body
        check.is_true(is_key_present(fault_data[0], "status"))
        check.equal(fault_data[0]["groupId"], group_id)
        check.equal(fault_data[0]["type"], "Tardy")

        # Delete schedule
        schedule.delete_schedule(auth, 200, schedule_id)


    def test_04_create_students_fault_absence(self, auth):
        faults = FaultsApi()
        schedule = ScheduleApi()

        group_id, schedule_id, student_id = get_student_data(auth)

        # Create fault
        fault_data = faults.post_create_student_faults(auth, 201, group_id, student_id['data'][3]['cedulaId'], "Absence", schedule_id)

        # Validate response body
        check.is_true(is_key_present(fault_data[0], "status"))
        check.equal(fault_data[0]["groupId"], group_id)
        check.equal(fault_data[0]["type"], "Absence")

        # Delete schedule
        schedule.delete_schedule(auth, 200, schedule_id)


    def test_05_get_alerts_student_count(self, auth):
        faults = FaultsApi()

        # Get alerts student count
        count_data = faults.get_faults_student_count(auth, 200)
        check.is_true(is_key_present(count_data, "count"))


    def test_06_put_justify_fault(self, auth):
        faults = FaultsApi()
        schedule = ScheduleApi()

        group_id, schedule_id, student_id = get_student_data(auth)

        # Create fault
        fault_data = faults.post_create_student_faults(auth, 201, group_id, student_id['data'][1]['cedulaId'],
                                                       "Absence", schedule_id)
        fault_id = fault_data[0]['id']

        # Justify absence
        justification_data = faults.put_justify_absence(auth, 200, fault_id)

        # Validate response data
        payload = put_justify_fault_payload()
        check.is_true(is_key_present(justification_data, "id"))
        check.equal(justification_data["justification"], payload["justification"])
        check.equal(justification_data["status"], "Justified")

        # Delete schedule
        schedule.delete_schedule(auth, 200, schedule_id)


    def test_07_get_students_faults(self, auth):
        faults = FaultsApi()
        schedule = ScheduleApi()

        group_id, schedule_id, student_id = get_student_data(auth)

        # Create fault
        faults.post_create_student_faults(auth, 201, group_id, student_id['data'][0]['cedulaId'], "Absence",
                                          schedule_id)

        # Get student faults
        faults_data = faults.get_student_faults(auth, 200)

        # Validate response data
        check.is_true(is_key_present(faults_data['data'][0], "id"))
        check.is_true(is_key_present(faults_data['data'][0], "group"))
        check.is_true(is_key_present(faults_data['data'][0], "tardies"))

        # Delete schedule
        schedule.delete_schedule(auth, 200, schedule_id)







