import json
import time

from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.student.student import *
from src.endpoints.users.users import *
from utils.asserts import *
from pytest_check import check
from utils.payloads.create_student import *


def create_random_field():
    time.sleep(1)
    epoch = datetime.datetime.today().strftime('%s')
    user_name = epoch
    return user_name


def create_parametrize_data():
    cedula_id = create_random_field()
    email = "user_student_" + create_random_field() + "@gmail.com"
    user_name = "user_student_" + create_random_field()
    return cedula_id, email, user_name


@pytest.mark.usefixtures("auth")
class TestStudentApi:

    def test_01_create_student_successful(self, auth):
        student = StudentApi()

        # Create student
        cedula_id, email, user_name = create_parametrize_data()
        response_data = student.post_create_student(auth, 201, cedula_id)

        # verify if id is present
        dictionary = response_data['created'][0]
        check.is_true(is_key_present(dictionary, "id"))

        # Delete the student to avoid unnecessary data
        student.delete_student_user(auth, 200, cedula_id)


    def test_02_create_existing_student_id(self, auth):
        student = StudentApi()

        # Create student
        cedula_id, email, user_name = create_parametrize_data()
        student.post_create_student(auth, 201, cedula_id)
        
        # Create student with existing cedula_id
        dictionary = student.post_create_student(auth, 201, cedula_id)
        error_message = dictionary['noCreated'][0]['error']
        check.equal(error_message, "El usuario ya existe")

        # Delete the student to avoid unnecessary data
        student.delete_student_user(auth, 200, cedula_id)
        student.delete_student_user(auth, 200, dictionary['created'][0]['id'])


    def test_03_get_all_student_users(self, auth):
        student = StudentApi

        # Get all students
        response_data = student.get_student_users(auth, 200)

        # Validate if the response has cedulaId and student
        dictionary = response_data['data'][0]
        check.is_true(is_key_present(dictionary, "cedulaId"))
        check.is_true(is_key_present(dictionary, "student"))


    def test_04_get_specific_student(self, auth):
        student = StudentApi()

        # Create student
        cedula_id, email, user_name = create_parametrize_data()
        student.post_create_student(auth, 201, cedula_id)
        
        # Get specific student
        dictionary = student.get_specific_student_user(auth, 200, cedula_id)

        # Validate the response body.
        check.is_true(is_key_present(dictionary, "id"))
        check.is_true(is_key_present(dictionary['studentGroup'], "groupId"))
        check.is_true(is_key_present(dictionary['studentGroup']['group'], "managerId"))

        # Delete the student to avoid unnecessary data
        student.delete_student_user(auth, 200, cedula_id)


    def test_05_edit_student(self, auth):
        student = StudentApi()

        # Create student
        cedula_id, email, user_name = create_parametrize_data()
        student.post_create_student(auth, 201, cedula_id)
        
        # Edit student
        dictionary = student.put_edit_student(auth, 200, cedula_id)

        # Verify if the response body contains ....
        payload = set_edit_student_payload(cedula_id)
        check.is_true(is_key_present(dictionary, "id"))
        check.is_true(is_key_present(dictionary, "tutor"))
        check.equal(int(cedula_id), int(payload["id"]))

        # Delete the student to avoid unnecessary data
        student.delete_student_user(auth, 200, cedula_id)


    def test_06_delete_student(self, auth):
        student = StudentApi()

        # Create student
        cedula_id, email, user_name = create_parametrize_data()
        student.post_create_student(auth, 201, cedula_id)

        # Delete student
        dictionary = student.delete_student_user(auth, 200, cedula_id)
        
        # Verify if the response body contains...
        check.is_true(is_key_present(dictionary, "id"))
        check.equal(int(cedula_id), int(dictionary["id"]))


    def test_07_get_student_report(self, auth):
        student = StudentApi()

        # Create student
        student_data = student.get_student_users(auth, 200)
        student_id = student_data['data'][0]['cedulaId']

        # Get student report
        report_data = student.get_student_report(auth, 200, student_id)

        # Verify if the response body contains...
        check.is_true(is_key_present(report_data, "absences"))
        check.is_true(is_key_present(report_data, "notes"))
        check.is_true(is_key_present(report_data, "faults"))

        
        
        





