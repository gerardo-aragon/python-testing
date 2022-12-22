import json
from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.administrator.administrator import *

@pytest.mark.usefixtures("auth")
class TestAdministratorApi:
    
    def test_create_admin_successful(self, auth):
        admin = AdministratorApi()
        dictionary = admin.post_create_administrator(auth, 201)
        
        
    def test_get(self, auth):
        admin = AdministratorApi()
        dictionary = admin.get_users(auth, 200)