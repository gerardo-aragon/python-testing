import datetime
import time

def set_create_student_payload(cedula_id):
    payload_create_student = [{
        "id": int(cedula_id),
        "firstName": "Student Automated",
        "lastName": "Upre",
        "birthdate": "09/11/1992",
        "tutor": "Tutor",
        "phone": 60606060,
        "address": "Dirección 01",
        "group": "7-1 (No eliminar)"
    }]
    return payload_create_student

def set_edit_student_payload(cedula_id):
    payload_edit_student = {
        "id": int(cedula_id),
        "firstName": "Student",
        "lastName": "Edited",
        "birthdate": "09/11/1990",
        "tutor": "Tutor edited",
        "phone": 70707070,
        "address": "Dirección edited",
        "group": "7-1 (No eliminar)"
    }
    return payload_edit_student
