import json
import time

from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.teacher.teacher import *
from src.endpoints.users.users import *
from utils.asserts import *
from pytest_check import check
from utils.payloads.create_teacher import *
from utils.preconditions import *


@pytest.mark.usefixtures("auth")
class TestTeacherApi:

    def test_01_create_teacher_successful(self, auth):
        teacher = TeacherApi()

        # Create teacher
        cedula_id, email, user_name = create_parametrize_data()
        response_data = teacher.post_create_teacher(auth, 201, cedula_id, "user_teacher_" + email,
                                                    "user_teacher_" + user_name)

        # verify if cedulaId is present
        dictionary = response_data['created'][0]
        check.is_true(is_key_present(dictionary, "cedulaId"))

        # Delete the teacher to avoid unnecessary data
        teacher.delete_teacher_user(auth, 200, cedula_id)

    def test_02_create_existing_teacher_id(self, auth):
        teacher = TeacherApi()

        # Create teacher
        cedula_id, email, user_name = create_parametrize_data()
        teacher.post_create_teacher(auth, 201, cedula_id, email, user_name)

        # Create teacher with existing cedula_id
        new_email = "user_teacher_" + create_random_fields() + "@gmail.com"
        new_user_name = "user_teacher_" + create_random_fields()
        response_data = teacher.post_create_teacher(auth, 201, cedula_id, new_email, new_user_name)
        error_message = response_data['noCreated'][0]['error']
        check.equal(error_message, "El usuario ya existe")

        # Delete the teacher to avoid unnecessary data
        teacher.delete_teacher_user(auth, 200, cedula_id)

    def test_03_create_existing_teacher_user(self, auth):
        teacher = TeacherApi()

        # Create teacher
        cedula_id, email, user_name = create_parametrize_data()
        teacher.post_create_teacher(auth, 201, cedula_id, "user_teacher_" + email, "user_teacher_" + user_name)

        # Create teacher with existing cedula_id
        new_cedula_id = create_random_fields()
        new_email = "user_teacher_" + create_random_fields() + "@gmail.com"
        response_data = teacher.post_create_teacher(auth, 201, new_cedula_id, new_email, user_name)
        error_message = response_data['noCreated'][0]['error']
        check.equal(error_message, "El usuario ya existe")

        # Delete the teacher to avoid unnecessary data
        teacher.delete_teacher_user(auth, 200, cedula_id)
        teacher.delete_teacher_user(auth, 200, new_cedula_id)

    def test_04_create_existing_teacher_email(self, auth):
        teacher = TeacherApi()

        # Create teacher
        cedula_id, email, user_name = create_parametrize_data()
        teacher.post_create_teacher(auth, 201, cedula_id, "user_teacher_" + email, "user_teacher_" + user_name)

        # Create teacher with existing cedula_id
        new_cedula_id = create_random_fields()
        new_user_name = "user_admin_" + create_random_fields()
        response_data = teacher.post_create_teacher(auth, 201, new_cedula_id, email, new_user_name)
        error_message = response_data['noCreated'][0]['error']
        check.equal(error_message, "El usuario ya existe")

        # Delete the teacher to avoid unnecessary data
        teacher.delete_teacher_user(auth, 200, cedula_id)
        teacher.delete_teacher_user(auth, 200, new_cedula_id)

    def test_05_get_all_teacher_users(self, auth):
        teacher = TeacherApi()
        # obtain all teacher users
        response_data = teacher.get_teacher_users(auth, 200)

        # get TEACHER role
        teacher_rol = response_data['data'][0]['role']

        # check if the obtained rol is equal to TEACHER
        check.equal(teacher_rol, "TEACHER")

        # check if cedulaId is present
        dictionary = response_data['data'][0]
        check.is_true(is_key_present(dictionary, "cedulaId"))

    def test_06_get_specific_user(self, auth):
        teacher = TeacherApi()
        user = UsersApi()

        # obtain all teacher uses
        response_data = teacher.get_teacher_users(auth, 200)

        # get teacher cedulaId
        admin_cedula_id = response_data['data'][0]['cedulaId']

        # get specific teacher
        dictionary = user.get_user(auth, 200, admin_cedula_id)

        # Verify if the response body contains ....
        check.is_true(is_key_present(dictionary, "email"))
        check.is_true(is_key_present(dictionary, "userName"))

    def test_07_edit_teacher_user_successful(self, auth):
        teacher = TeacherApi()

        # Create teacher if there are no teachers
        cedula_id, email, user_name = create_parametrize_data()
        response_data = teacher.post_create_teacher(auth, 201, cedula_id, "user_teacher_" + email,
                                                    "user_teacher_" + user_name)

        # Get cedula_id
        teacher_id = response_data['created'][0]['cedulaId']

        # Create new teacher data
        new_email = "edited_teacher_" + create_random_fields() + "@gmail.com"
        new_user_name = "edited_teacher_" + create_random_fields()

        # Edit the teacher
        dictionary = teacher.put_edit_teacher(auth, 200, teacher_id, new_email, new_user_name)

        # Verify if the response body contains ....
        check.is_true(is_key_present(dictionary, "email"))
        check.is_true(is_key_present(dictionary, "userName"))

        # Verify if the data was edited correctly
        check.equal(dictionary['email'], new_email)

        # Delete the teacher to avoid unnecessary data
        teacher.delete_teacher_user(auth, 200, cedula_id)

    def test_08_edit_teacher_existing_email(self, auth):
        teacher = TeacherApi()

        # Create teacher if there are no admins
        teacher01_id, teacher01_email, teacher01_user_name = create_parametrize_data()
        teacher.post_create_teacher(auth, 201, teacher01_id, "user_teacher_" + teacher01_email,
                                    "user_teacher_" + teacher01_user_name)

        teacher02_id, teacher02_email, teacher02_user_name = create_parametrize_data()
        teacher.post_create_teacher(auth, 201, teacher02_id, "user_teacher_" + teacher02_email,
                                    "user_teacher_" + teacher02_user_name)

        # Create parametrized fields
        user_name = "edited_" + create_random_fields()

        # Edit the teacher
        dictionary = teacher.put_edit_teacher(auth, 400, teacher02_id, "user_teacher_" + teacher01_email,
                                              "user_teacher_" + user_name)
        error_message = dictionary['message']
        check.equal(error_message, "Bad request: User email already taken")

        # Delete the teacher to avoid unnecessary data
        teacher.delete_teacher_user(auth, 200, teacher01_id)
        teacher.delete_teacher_user(auth, 200, teacher02_id)

    def test_09_edit_teacher_existing_user_name(self, auth):
        teacher = TeacherApi()

        # Create teacher if there are no admins
        teacher01_id, teacher01_email, teacher01_user_name = create_parametrize_data()
        teacher.post_create_teacher(auth, 201, teacher01_id, "user_teacher_" + teacher01_email,
                                    "user_teacher_" + teacher01_user_name)

        teacher02_id, teacher02_email, teacher02_user_name = create_parametrize_data()
        teacher.post_create_teacher(auth, 201, teacher02_id, "user_teacher_" + teacher02_email,
                                    "user_teacher_" + teacher02_user_name)

        # Create parametrized fields
        email = "edited_" + create_random_fields() + "@gmail.com"

        # Edit the teacher
        dictionary = teacher.put_edit_teacher(auth, 400, teacher02_id, email, "user_teacher_" + teacher01_user_name)
        error_message = dictionary['message']
        check.equal(error_message, "Bad request: User name already taken")

        # Delete the teacher to avoid unnecessary data
        teacher.delete_teacher_user(auth, 200, teacher01_id)
        teacher.delete_teacher_user(auth, 200, teacher02_id)

    def test_10_delete_teacher_user(self, auth):
        teacher = TeacherApi()

        # Create teacher if there are no admins
        cedula_id, email, user_name = create_parametrize_data()
        teacher.post_create_teacher(auth, 201, cedula_id, "user_teacher_" + email, "user_teacher_" + user_name)

        # Delete the teacher
        dictionary = teacher.delete_teacher_user(auth, 200, cedula_id)

        # Validate the deleted id
        deleted_id = dictionary['id']
        check.equal(deleted_id, int(cedula_id))
        check.is_true(is_key_present(dictionary, "id"))
