import json
import time

from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.administrator.administrator import *
from src.endpoints.users.users import *
from utils.asserts import *
from pytest_check import check
from utils.payloads.create_administrator import *

def create_random_field():
    time.sleep(1)
    epoch = datetime.datetime.today().strftime('%s')
    user_name = epoch
    return user_name

def create_parametrize_data():
    cedula_id = create_random_field()
    email = "user_admin_" + create_random_field() + "@gmail.com"
    user_name = "user_admin_" + create_random_field()
    return cedula_id, email, user_name

@pytest.mark.usefixtures("auth")
class TestAdministratorApi:


    def test_01_create_admin_successful(self, auth):
        admin = AdministratorApi()
        
        # Create admin
        cedula_id, email, user_name = create_parametrize_data()
        response_data = admin.post_create_administrator(auth, 201, cedula_id, email, user_name)
        
        # verify if cedulaId is present
        dictionary = response_data['created'][0]
        check.is_true(is_key_present(dictionary, "cedulaId"))
        
        
    def test_02_create_existing_admin_id(self, auth):
        admin = AdministratorApi()

        # Create admin
        cedula_id, email, user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, cedula_id, email, user_name)
        
        # Create admin with existing cedula_id
        new_email = "user_admin_" + create_random_field() + "@gmail.com"
        new_user_name = "user_admin_" + create_random_field()
        response_data = admin.post_create_administrator(auth, 201, cedula_id, new_email, new_user_name)
        error_message = response_data['noCreated'][0]['error']
        check.equal(error_message, "El usuario ya existe")

    # Pude crear un admin con user_name existente
    def test_03_create_existing_admin_user(self, auth):
        admin = AdministratorApi()

        # Create admin
        cedula_id, email, user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, cedula_id, email, user_name)

        # Create admin with existing cedula_id
        new_cedula_id = create_random_field()
        new_email = "user_admin_" + create_random_field() + "@gmail.com"
        response_data = admin.post_create_administrator(auth, 201, new_cedula_id, new_email, user_name)
        error_message = response_data['noCreated'][0]['error']
        check.equal(error_message, "El usuario ya existe")
        

    # Pude crear un admin con email existente
    def test_04_create_existing_admin_email(self, auth):
        admin = AdministratorApi()

        # Create admin
        cedula_id, email, user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, cedula_id, email, user_name)

        # Create admin with existing cedula_id
        new_cedula_id = create_random_field()
        new_user_name = "user_admin_" + create_random_field()
        response_data = admin.post_create_administrator(auth, 201, new_cedula_id, email, new_user_name)
        error_message = response_data['noCreated'][0]['error']
        check.equal(error_message, "El usuario ya existe")


    def test_05_get_all_admin_users(self, auth):
        admin = AdministratorApi()
        # obtain all admin uses
        response_data = admin.get_admin_users(auth, 200)

        # get admin role
        admin_rol = response_data['data'][0]['role']

        # check if the obtained rol is equal to ADMIN
        check.equal(admin_rol,"ADMIN")

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
        admin_data = admin.post_create_administrator(auth, 201, cedula_id, email, user_name)
        
        # Obtain cedulaId to edit the admin
        admin_id = admin_data['created'][0]['cedulaId']
        
        # Create parametrized fields
        email = "edited_admin" + create_random_field() + "@gmail.com"
        user_name = "edited_admin" + create_random_field()
        
        # Edit the admin 
        dictionary = admin.put_edit_administrator(auth, 200, admin_id, email, user_name)

        # Verify if the response body contains ....
        check.is_true(is_key_present(dictionary, "email"))
        check.is_true(is_key_present(dictionary, "userName"))

        # Verify if the data was edited correctly
        check.equal(dictionary['email'], email)


    def test_08_edit_admin_user_existing_email(self, auth):
        admin = AdministratorApi()

        # Create admin if there are no admins
        cedula_id, email, user_name = create_parametrize_data()
        admin_data = admin.post_create_administrator(auth, 201, cedula_id, email, user_name)

        # Obtain email to edit the admin
        existing_email = admin_data['created'][0]['email']

        # Create parametrized fields
        user_name = "edited_" + create_random_field()

        # Edit the admin
        dictionary = admin.put_edit_administrator(auth, 200, cedula_id, existing_email, user_name)
        error_message = dictionary['noCreated'][0]['error']
        check.equal(error_message, "El usuario ya existe")


    def test_09_edit_admin_existing_user_name(self, auth):
        admin = AdministratorApi()

        # Create admin if there are no admins
        cedula_id, email, user_name = create_parametrize_data()
        admin_data = admin.post_create_administrator(auth, 201, cedula_id, email, user_name)

        # Obtain userName to edit the admin
        existing_user_name = admin_data['created'][0]['userName']

        # Create parametrized fields
        email = "edited_" + create_random_field() + "@gmail.com"

        # Edit the admin
        dictionary = admin.put_edit_administrator(auth, 200, cedula_id, email, existing_user_name)
        error_message = dictionary['noCreated'][0]['error']
        check.equal(error_message, "El usuario ya existe")
        
        
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
        



        

