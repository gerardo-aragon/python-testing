from datetime import datetime, timedelta

def set_create_fault_payload(group_id, student_id, fault_type):
    payload_create_fault = {
        "groupId": group_id,
        "userId": 503890884,
        "startDate": str(datetime.now().date() + timedelta(days=1)) + "T13:30:21Z",
        "endDate": str(datetime.now().date() + timedelta(days=1)) + "T13:30:48Z",
        "studentId": student_id,
        "startTime": "07:00",
        "endTime": "07:40",
        "status": "Unjustified",
        "justification": "Unjustified",
        "type": fault_type
    }
    return payload_create_fault