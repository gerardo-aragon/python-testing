import datetime
import time


def set_create_group_payload(group_name):
    payload_create_group = [{
        "name": group_name,
        "managerUsername": "luis.ponce"
    }]
    return payload_create_group



def set_edit_group_payload(group_name):
    payload_edit_group = {
        "name": group_name,
        "managerId": 208340998
    }
    return payload_edit_group