import json
import time

from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.administrator.administrator import *
from src.endpoints.users.users import *
from utils.asserts import *
from pytest_check import check
from utils.payloads.create_administrator import *


@pytest.mark.usefixtures("auth")
class TestAdministratorApi:
    
    def test_01_create_admin_successful(self, auth):
        admin = AdministratorApi()
        response_data = admin.post_create_administrator(auth, 201)
        # verify if cedulaId is present
        dictionary = response_data['created'][0]
        check.is_true(is_key_present(dictionary, "cedulaId"))
        
        
    def test_02_create_existing_id(self, auth):
        admin = AdministratorApi()
        response_data = admin.get_users(auth, 200)
        cedula_id = response_data['data'][0]['cedulaId']
        print(cedula_id)


    def test_03_get_all_admin_users(self, auth):
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
    
    
    def test_04_get_specific_user(self, auth):
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
        
        
    def test_05_edit_admin_user(self, auth):
        admin = AdministratorApi()
        admin_data = admin.post_create_administrator(auth, 201)
        # Obtain cedulaId to edit the admin
        # print(admin_data)
        admin_id = admin_data['created'][0]['cedulaId']
        dictionary = admin.put_edit_administrator(auth, 200, admin_id)
        # Verify if the response body contains ....
        check.is_true(is_key_present(dictionary, "email"))
        check.is_true(is_key_present(dictionary, "userName"))
        # Verify if the data was edited correctly
        payload = payload_edit_admin
        check.equal(dictionary['email'], payload['email'])
        
        



        

