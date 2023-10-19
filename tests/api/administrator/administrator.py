import json
import time

from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.administrator.administrator import *
from src.endpoints.users.users import *
from utils.asserts import *
from pytest_check import check
from utils.payloads.create_administrator import *
from utils.preconditions import *


@pytest.mark.usefixtures("auth")
class TestAdministratorApi:

    def test_01_create_admin_successful(self, auth):
        admin = AdministratorApi()

        # Create admin
        cedula_id, email, user_name = create_parametrize_data()
        response_data = admin.post_create_administrator(auth, 201, cedula_id, "user_admin_" + email,
                                                        "user_admin_" + user_name)

        # verify if cedulaId is present
        dictionary = response_data['created'][0]
        check.is_true(is_key_present(dictionary, "cedulaId"))

        # Delete the admin to avoid unnecessary data
        admin.delete_admin_user(auth, 200, cedula_id)

    def test_02_create_existing_admin_id(self, auth):
        admin = AdministratorApi()

        # Create admin
        cedula_id, email, user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, cedula_id, "user_admin_" + email, "user_admin_" + user_name)

        # Create admin with existing cedula_id
        new_email = "user_admin_" + create_random_fields() + "@gmail.com"
        new_user_name = "user_admin_" + create_random_fields()
        response_data = admin.post_create_administrator(auth, 201, cedula_id, new_email, new_user_name)
        error_message = response_data['noCreated'][0]['error']
        check.equal(error_message, "El usuario ya existe")

        # Delete the admin to avoid unnecessary data
        admin.delete_admin_user(auth, 200, cedula_id)

    # Pude crear un admin con user_name existente
    def test_03_create_existing_admin_user(self, auth):
        admin = AdministratorApi()

        # Create admin
        cedula_id, email, user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, cedula_id, email, user_name)

        # Create admin with existing user_name
        new_cedula_id = create_random_fields()
        new_email = "user_admin_" + create_random_fields() + "@gmail.com"
        response_data = admin.post_create_administrator(auth, 201, new_cedula_id, new_email, user_name)
        error_message = response_data['noCreated'][0]['error']
        check.equal(error_message, "El usuario ya existe")

        # Delete the admin to avoid unnecessary data
        admin.delete_admin_user(auth, 200, cedula_id)
        admin.delete_admin_user(auth, 200, response_data['created'][0]['cedulaId'])

    # Pude crear un admin con email existente
    def test_04_create_existing_admin_email(self, auth):
        admin = AdministratorApi()

        # Create admin
        cedula_id, email, user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, cedula_id, email, user_name)

        # Create admin with existing cedula_id
        new_cedula_id = create_random_fields()
        new_user_name = "user_admin_" + create_random_fields()
        response_data = admin.post_create_administrator(auth, 201, new_cedula_id, email, new_user_name)
        error_message = response_data['noCreated'][0]['error']
        check.equal(error_message, "El usuario ya existe")

        # Delete the admin to avoid unnecessary data
        admin.delete_admin_user(auth, 200, cedula_id)
        admin.delete_admin_user(auth, 200, response_data['created'][0]['cedulaId'])

    def test_05_get_all_admin_users(self, auth):
        admin = AdministratorApi()
        # obtain all admin uses
        response_data = admin.get_admin_users(auth, 200)

        # get admin role
        admin_rol = response_data['data'][0]['role']

        # check if the obtained rol is equal to ADMIN
        check.equal(admin_rol, "ADMIN")

        # check if cedulaId is present
        dictionary = response_data['data'][0]
        check.is_true(is_key_present(dictionary, "cedulaId"))

    def test_06_get_specific_user(self, auth):
        admin = AdministratorApi()
        user = UsersApi()

        # obtain all admin uses
        response_data = admin.get_admin_users(auth, 200)

        # get admin cedulaId
        admin_cedula_id = response_data['data'][0]['cedulaId']

        # get specific admin
        dictionary = user.get_user(auth, 200, admin_cedula_id)

        # Verify if the response body contains ....
        check.is_true(is_key_present(dictionary, "email"))
        check.is_true(is_key_present(dictionary, "userName"))

    def test_07_edit_admin_user_successful(self, auth):
        admin = AdministratorApi()

        # Create admin if there are no admins
        cedula_id, email, user_name = create_parametrize_data()
        admin_data = admin.post_create_administrator(auth, 201, cedula_id, "user_admin_" + email,
                                                     "user_admin_" + user_name)

        # Obtain cedulaId to edit the admin
        admin_id = admin_data['created'][0]['cedulaId']

        # Create parametrized fields
        email = "edited_admin" + create_random_fields() + "@gmail.com"
        user_name = "edited_admin" + create_random_fields()

        # Edit the admin 
        dictionary = admin.put_edit_administrator(auth, 200, admin_id, email, user_name)

        # Verify if the response body contains ....
        check.is_true(is_key_present(dictionary, "email"))
        check.is_true(is_key_present(dictionary, "userName"))

        # Verify if the data was edited correctly
        check.equal(dictionary['email'], email)

        # Delete the admin to avoid unnecessary data
        admin.delete_admin_user(auth, 200, cedula_id)

    def test_08_edit_admin_user_existing_email(self, auth):
        admin = AdministratorApi()

        # Create admin if there are no admins
        admin01_id, admin01_email, admin01_user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, admin01_id, "user_admin_" + admin01_email,
                                        "user_admin_" + admin01_user_name)

        admin02_id, admin02_email, admin02_user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, admin02_id, "user_admin_" + admin02_email,
                                        "user_admin_" + admin02_user_name)

        # Create parametrized fields
        user_name = "edited_user_admin" + create_random_fields()

        # Edit the admin
        dictionary = admin.put_edit_administrator(auth, 400, admin02_id, "user_admin_" + admin01_email, user_name)
        error_message = dictionary['message']
        check.equal(error_message, "Bad request: User email already taken")

        # Delete the admin to avoid unnecessary data
        admin.delete_admin_user(auth, 200, admin01_id)
        admin.delete_admin_user(auth, 200, admin02_id)

    def test_09_edit_admin_existing_user_name(self, auth):
        admin = AdministratorApi()

        # Create admin if there are no admins
        admin01_id, admin01_email, admin01_user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, admin01_id, "user_admin_" + admin01_email,
                                        "user_admin_" + admin01_user_name)

        admin02_id, admin02_email, admin02_user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, admin02_id, "user_admin_" + admin02_email,
                                        "user_admin_" + admin02_user_name)

        # Create parametrized fields
        email = "edited_user_admin" + create_random_fields() + "@gmail.com"

        # Edit the admin
        dictionary = admin.put_edit_administrator(auth, 400, admin02_id, email, "user_admin_" + admin01_user_name)
        error_message = dictionary['message']
        check.equal(error_message, "Bad request: User name already taken")

        # Delete the admin to avoid unnecessary data
        admin.delete_admin_user(auth, 200, admin01_id)
        admin.delete_admin_user(auth, 200, admin02_id)

    def test_10_delete_admin_user(self, auth):
        admin = AdministratorApi()

        # Create admin if there are no admins
        cedula_id, email, user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, cedula_id, email, user_name)

        # Edit the admin
        dictionary = admin.delete_admin_user(auth, 200, cedula_id)

        # Validate the deleted id
        deleted_id = dictionary['id']
        check.equal(deleted_id, int(cedula_id))
        check.is_true(is_key_present(dictionary, "id"))
