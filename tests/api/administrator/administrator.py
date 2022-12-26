import json
from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.administrator.administrator import *
from utils.asserts import *
from pytest_check import check


@pytest.mark.usefixtures("auth")
class TestAdministratorApi:
    
    def test_create_admin_successful(self, auth):
        admin = AdministratorApi()
        response_data = admin.post_create_administrator(auth, 201)
        # verify if cedulaId is present
        dictionary = response_data['created'][0]
        check.is_true(is_key_present(dictionary, "cedulaId"))
        # print(dictionary)
        
        
    # pendiente, como pasar los datos que son repetidos? debereian ser parametros?
    def test_create_existing_id(self, auth):
        admin = AdministratorApi()
        response_data = admin.get_users(auth, 200)
        cedula_id = response_data['data'][0]['cedulaId']
        print(cedula_id)


    def test_get_admin_users(self, auth):
        admin = AdministratorApi()
        # obtain all admin uses
        response_data = admin.get_users(auth, 200)
        # get admin role
        admin_rol = response_data['data'][0]['role']
        # check if the obtained rol is equal to ADMIN
        check.equal(admin_rol,"ADMIN")
        # check if cedulaId is present
        dictionary = response_data['data'][0]
        check.is_true(is_key_present(dictionary, "cedulaId"))


    def test_edit_admin_user(self, auth):


        

