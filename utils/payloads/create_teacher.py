import datetime
import time

def set_create_teacher_payload(cedula_id, email, user_name):
    payload_create_teacher = [{
        "cedulaId": int(cedula_id),
        "firstName": "Teacher",
        "lastName": "Upre",
        "birthdate": "09/11/1992",
        "phone": 60606060,
        "email": str(email),
        "userName": str(user_name),
        "password": "Test123@"
    }]
    return payload_create_teacher

def set_edit_teacher_payload(email, user_name):
    payload_edit_teacher = {
        "firstName": "Teacher",
        "lastName": "Upre edited",
        "birthdate": "09/11/1999",
        "phone": 70707070,
        "email": str(email),
        "userName": str(user_name),
        "password": "Edited123@"
    }
    return payload_edit_teacher

