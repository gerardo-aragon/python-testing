import datetime
import time

def set_create_admin_payload(cedula_id, email, user_name):
    payload_create_admin = [{
        "cedulaId": int(cedula_id),
        "firstName": "Admin",
        "lastName": "Postman",
        "birthdate": "09/11/1992",
        "phone": 60606060,
        "email": str(email),
        "userName": str(user_name),
        "password": "Test123@"
    }]
    return payload_create_admin

def set_edit_admin_payload(email, user_name):
    payload_edit_admin = {
        "firstName": "Admin edited",
        "lastName": "Postman edited",
        "birthdate": "09/11/1999",
        "phone": 70707070,
        "email": str(email),
        "userName": str(user_name),
        "password": "Edited123@"
    }
    return payload_edit_admin

