from datetime import datetime, timedelta

def set_create_attendance_payload(schedule_id, teacher_id, group_id, student_id, start_time, end_time, attendance_type):
    payload_create_attendance = {
        "scheduleId": schedule_id,
        "faults": [
            {
                "userId": teacher_id,
                "groupId": group_id,
                "studentId": student_id,
                "justification": "Unjustified",
                "startTime": start_time,
                "endTime": end_time,
                "status": "Unjustified",
                "startDate": str(datetime.now().date()) + "T13:30:21Z",
                "endDate": str(datetime.now().date()) + "T13:30:21Z",
                "type": attendance_type
            },
        ]
    }
    return payload_create_attendance