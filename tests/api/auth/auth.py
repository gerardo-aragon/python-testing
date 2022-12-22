import json
from utils.api_helper import *
from src.endpoints.auth.auth import *


class TestAuthenticateApi:
    def test_authenticate_success(self):
        auth = AuthenticationApi()
        response_data = auth.authenticate("gerardo.aragon", "Test123@", 201)
        
        




    
        
    
    