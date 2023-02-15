import json
import time

from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.schedule.schedule import *
from utils.asserts import *
from pytest_check import check
from utils.payloads.create_schedule import *
from src.endpoints.groups.groups import *
from utils.preconditions import *


@pytest.mark.usefixtures("auth")
class TestScheduleApi:

    def test_01_create_schedule_successful(self, auth):
        schedule = ScheduleApi()
        group = GroupsApi()

        # Search an existent group (Created previously by database)
        search_group = group.get_search_group(auth, 200, "7-1 (No eliminar)")
        group_id = search_group["data"][0]["id"]

        # Create schedule
        schedule_name = "Horario " + (create_random_fields()[-5:])
        dictionary = schedule.post_create_schedule(auth, 201, schedule_name, group_id)
        schedule_id = dictionary["id"]

        # verify if id is present
        check.equal(dictionary["groupId"], group_id)
        check.equal(dictionary["name"], schedule_name)
        check.is_true(is_key_present(dictionary["scheduleJson"], "monday"))

        # Delete the schedule to avoid unnecessary data
        schedule.delete_schedule(auth, 200, schedule_id)


    def test_02_get_schedule_by_group_id(self, auth):
        schedule = ScheduleApi()
        group = GroupsApi()

        # Search an existent group (Created previously by database)
        search_group = group.get_search_group(auth, 200, "7-1 (No eliminar)")
        group_id = search_group["data"][0]["id"]

        # Create a group if there are no groups
        schedule_name = "Horario " + (create_random_fields()[-5:])
        new_schedule = schedule.post_create_schedule(auth, 201, schedule_name, group_id)
        schedule_id = new_schedule["id"]

        # Get schedules by group id
        dictionary = schedule.get_all_schedule_by_group_id(auth, 200, group_id)

        # verify if id is present
        check.is_true(is_key_present(dictionary[0], "groupId"))
        check.is_true(is_key_present(dictionary[0], "name"))
        check.is_true(is_key_present(dictionary[0]["scheduleJson"], "monday"))

        # Delete the schedule to avoid unnecessary data
        schedule.delete_schedule(auth, 200, schedule_id)


    def test_03_get_schedule_by_id(self, auth):
        schedule = ScheduleApi()
        group = GroupsApi()

        # Search an existent group (Created previously by database)
        search_group = group.get_search_group(auth, 200, "7-1 (No eliminar)")
        group_id = search_group["data"][0]["id"]

        # Create a group if there are no groups
        schedule_name = "Horario " + (create_random_fields()[-5:])
        new_schedule = schedule.post_create_schedule(auth, 201, schedule_name, group_id)
        schedule_id = new_schedule["id"]

        # Get schedules by group id
        dictionary = schedule.get_schedule_by_id(auth, 200, schedule_id)

        # verify if id is present
        check.is_true(is_key_present(dictionary, "groupId"))
        check.is_true(is_key_present(dictionary, "name"))
        check.is_true(is_key_present(dictionary["scheduleJson"], "monday"))

        # Delete the schedule to avoid unnecessary data
        schedule.delete_schedule(auth, 200, schedule_id)


    def test_04_update_schedule(self, auth):
        schedule = ScheduleApi()
        group = GroupsApi()

        # Search an existent group (Created previously by database)
        search_group = group.get_search_group(auth, 200, "7-1 (No eliminar)")
        group_id = search_group["data"][0]["id"]

        # Create a group if there are no groups
        schedule_name = "Horario " + (create_random_fields()[-5:])
        new_schedule = schedule.post_create_schedule(auth, 201, schedule_name, group_id)
        schedule_id = new_schedule["id"]

        # Get schedules by group id
        new_schedule_name = "edited_" + "Horario " + (create_random_fields()[-5:])
        dictionary = schedule.put_edit_schedule(auth, 200, schedule_id, group_id, new_schedule_name)

        # verify if id is present
        check.is_true(is_key_present(dictionary, "groupId"))
        check.is_true(is_key_present(dictionary, "name"))
        check.is_true(is_key_present(dictionary["scheduleJson"], "monday"))

        # Delete the schedule to avoid unnecessary data
        schedule.delete_schedule(auth, 200, schedule_id)


    def test_05_delete_schedule(self, auth):
        schedule = ScheduleApi()
        group = GroupsApi()

        # Search an existent group (Created previously by database)
        search_group = group.get_search_group(auth, 200, "7-1 (No eliminar)")
        group_id = search_group["data"][0]["id"]

        # Create a group if there are no groups
        schedule_name = "Horario " + (create_random_fields()[-5:])
        new_schedule = schedule.post_create_schedule(auth, 201, schedule_name, group_id)
        schedule_id = new_schedule["id"]

        # Delete the schedule to avoid unnecessary data
        schedule.delete_schedule(auth, 200, schedule_id)




