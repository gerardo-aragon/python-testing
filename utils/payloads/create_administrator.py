import datetime
import time

def create_random_field():
    epoch = datetime.datetime.today().strftime('%s')
    user_name = epoch
    return user_name

payload_create_admin = [{
    "cedulaId": int(create_random_field()),
    "firstName": "Admin",
    "lastName": "Postman",
    "birthdate": "09/11/1992",
    "phone": 60606060,
    "email": str("user_admin_" + create_random_field() + "@gmail.com"),
    "userName": str("user_admin_" + create_random_field()),
    "password": "Test123@"
}]


payload_edit_admin = {
    "firstName": "Admin edited",
    "lastName": "Postman edited",
    "birthdate": "09/11/1999",
    "phone": 70707070,
    "email": str("edited_" + create_random_field() + "@gmail.com"),
    "userName": str("edited_" + create_random_field()),
    "password": "Edited123@"
}

