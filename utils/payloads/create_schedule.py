import datetime
import time


def set_create_schedule_payload(schedule_name, group_id):
    payload_create_schedule = {
   "groupId":group_id,
   "name":schedule_name,
   "scheduleJson":{
      "monday":{
         "morning":[
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":1,
               "start":"07:00",
               "end":"07:40"
            },
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":2,
               "start":"07:40",
               "end":"08:20"
            },
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":3,
               "start":"08:30",
               "end":"09:10"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":4,
               "start":"09:10",
               "end":"09:50"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":5,
               "start":"10:10",
               "end":"10:50"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":6,
               "start":"10:50",
               "end":"11:30"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":7,
               "start":"11:35",
               "end":"12:15"
            }
         ],
         "afternoon":[
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":1,
               "start":"12:30",
               "end":"13:10"
            },
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":2,
               "start":"13:10",
               "end":"13:50"
            },
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":3,
               "start":"14:10",
               "end":"14:50"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":4,
               "start":"14:50",
               "end":"15:30"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":5,
               "start":"15:35",
               "end":"16:15"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":6,
               "start":"16:15",
               "end":"16:55"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":7,
               "start":"17:00",
               "end":"17:40"
            }
         ]
      },
      "tuesday":{
         "morning":[
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":1,
               "start":"07:00",
               "end":"07:40"
            },
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":2,
               "start":"07:40",
               "end":"08:20"
            },
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":3,
               "start":"08:30",
               "end":"09:10"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":4,
               "start":"09:10",
               "end":"09:50"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":5,
               "start":"10:10",
               "end":"10:50"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":6,
               "start":"10:50",
               "end":"11:30"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":7,
               "start":"11:35",
               "end":"12:15"
            }
         ],
         "afternoon":[
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":1,
               "start":"12:30",
               "end":"13:10"
            },
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":2,
               "start":"13:10",
               "end":"13:50"
            },
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":3,
               "start":"14:10",
               "end":"14:50"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":4,
               "start":"14:50",
               "end":"15:30"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":5,
               "start":"15:35",
               "end":"16:15"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":6,
               "start":"16:15",
               "end":"16:55"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":7,
               "start":"17:00",
               "end":"17:40"
            }
         ]
      },
      "wednesday":{
         "morning":[
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":1,
               "start":"07:00",
               "end":"07:40"
            },
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":2,
               "start":"07:40",
               "end":"08:20"
            },
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":3,
               "start":"08:30",
               "end":"09:10"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":4,
               "start":"09:10",
               "end":"09:50"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":5,
               "start":"10:10",
               "end":"10:50"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":6,
               "start":"10:50",
               "end":"11:30"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":7,
               "start":"11:35",
               "end":"12:15"
            }
         ],
         "afternoon":[
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":1,
               "start":"12:30",
               "end":"13:10"
            },
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":2,
               "start":"13:10",
               "end":"13:50"
            },
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":3,
               "start":"14:10",
               "end":"14:50"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":4,
               "start":"14:50",
               "end":"15:30"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":5,
               "start":"15:35",
               "end":"16:15"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":6,
               "start":"16:15",
               "end":"16:55"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":7,
               "start":"17:00",
               "end":"17:40"
            }
         ]
      },
      "thursday":{
         "morning":[
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":1,
               "start":"07:00",
               "end":"07:40"
            },
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":2,
               "start":"07:40",
               "end":"08:20"
            },
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":3,
               "start":"08:30",
               "end":"09:10"
            },
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":4,
               "start":"09:10",
               "end":"09:50"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":5,
               "start":"10:10",
               "end":"10:50"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":6,
               "start":"10:50",
               "end":"11:30"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":7,
               "start":"11:35",
               "end":"12:15"
            }
         ],
         "afternoon":[
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":1,
               "start":"12:30",
               "end":"13:10"
            },
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":2,
               "start":"13:10",
               "end":"13:50"
            },
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":3,
               "start":"14:10",
               "end":"14:50"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":4,
               "start":"14:50",
               "end":"15:30"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":5,
               "start":"15:35",
               "end":"16:15"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":6,
               "start":"16:15",
               "end":"16:55"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":7,
               "start":"17:00",
               "end":"17:40"
            }
         ]
      },
      "friday":{
         "morning":[
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":1,
               "start":"07:00",
               "end":"07:40"
            },
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":2,
               "start":"07:40",
               "end":"08:20"
            },
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":3,
               "start":"08:30",
               "end":"09:10"
            },
            {
               "courseId":"2",
               "teacherId":"",
               "lessonId":4,
               "start":"09:10",
               "end":"09:50"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":5,
               "start":"10:10",
               "end":"10:50"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":6,
               "start":"10:50",
               "end":"11:30"
            },
            {
               "courseId":"3",
               "teacherId":"",
               "lessonId":7,
               "start":"11:35",
               "end":"12:15"
            }
         ],
         "afternoon":[
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":1,
               "start":"12:30",
               "end":"13:10"
            },
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":2,
               "start":"13:10",
               "end":"13:50"
            },
            {
               "courseId":"1",
               "teacherId":"",
               "lessonId":3,
               "start":"14:10",
               "end":"14:50"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":4,
               "start":"14:50",
               "end":"15:30"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":5,
               "start":"15:35",
               "end":"16:15"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":6,
               "start":"16:15",
               "end":"16:55"
            },
            {
               "courseId":"4",
               "teacherId":"",
               "lessonId":7,
               "start":"17:00",
               "end":"17:40"
            }
         ]
      }
   }
}
    return payload_create_schedule


def set_edit_schedule_payload(schedule_id, group_id, schedule_name):
   payload_edit_schedule = {
   "id": schedule_id,
   "groupId": group_id,
   "name": schedule_name,
   "scheduleJson": {
      "monday": {
         "morning": [
            {
               "courseId": "3",
               "teacherId": "503890884",
               "lessonId": 1,
               "start": "07:00",
               "end": "07:40"
            },
            {
               "courseId": "3",
               "teacherId": "503890884",
               "lessonId": 2,
               "start": "07:40",
               "end": "08:20"
            },
            {
               "courseId": "3",
               "teacherId": "503890884",
               "lessonId": 3,
               "start": "08:30",
               "end": "09:10"
            },
            {
               "courseId": "3",
               "teacherId": "503890884",
               "lessonId": 4,
               "start": "09:10",
               "end": "09:50"
            },
            {
               "courseId": "3",
               "teacherId": "503890884",
               "lessonId": 5,
               "start": "10:10",
               "end": "10:50"
            },
            {
               "courseId": "3",
               "teacherId": "503890884",
               "lessonId": 6,
               "start": "10:50",
               "end": "11:30"
            },
            {
               "courseId": "3",
               "teacherId": "503890884",
               "lessonId": 7,
               "start": "11:35",
               "end": "12:15"
            }
         ],
         "afternoon": [

         ]
      },
      "tuesday": {
         "morning": [
            {
               "courseId": "3",
               "teacherId": "503890884",
               "lessonId": 1,
               "start": "07:00",
               "end": "07:40"
            },
            {
               "courseId": "3",
               "teacherId": "503890884",
               "lessonId": 2,
               "start": "07:40",
               "end": "08:20"
            }
         ],
         "afternoon": [

         ]
      },
      "wednesday": {
         "morning": [

         ],
         "afternoon": [

         ]
      },
      "thursday": {
         "morning": [

         ],
         "afternoon": [

         ]
      },
      "friday": {
         "morning": [

         ],
         "afternoon": [

         ]
      }
   }
}
   return payload_edit_schedule
