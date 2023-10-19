import json
import time

from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.groups.groups import *
from utils.asserts import *
from pytest_check import check
from utils.payloads.create_groups import *
from utils.preconditions import *


@pytest.mark.usefixtures("auth")
class TestGroupApi:

    def test_01_create_group_successful(self, auth):
        group = GroupsApi()

        # Create group
        group_name = "Sección " + (create_random_fields()[-5:])
        response_data = group.post_create_groups(auth, 201, group_name)

        # verify if id is present
        dictionary = response_data['created'][0]
        check.is_true(is_key_present(dictionary, "id"))

        # Delete the group to avoid unnecessary data
        group.delete_group(auth, 200, response_data['created'][0]['id'])

    def test_02_create_existing_group(self, auth):
        group = GroupsApi()

        # Create group
        group_name = "Sección " + (create_random_fields()[-5:])
        group.post_create_groups(auth, 201, group_name)

        # Create group with existing name
        dictionary = group.post_create_groups(auth, 201, group_name)
        error_message = dictionary['noCreated'][0]['error']
        check.equal(error_message, "El grupo ya existe")

        # Delete the group to avoid unnecessary data
        group.delete_group(auth, 200, dictionary['created'][0]['id'])

    def test_03_get_all_groups(self, auth):
        group = GroupsApi()

        # Create group if there are no groups
        group_name = "Sección " + (create_random_fields()[-5:])
        response = group.post_create_groups(auth, 201, group_name)

        # Get all groups
        response_data = group.get_all_groups(auth, 200)

        # Validate if the response has valid data
        dictionary = response_data['data'][0]
        check.is_true(is_key_present(dictionary, "name"))
        check.is_true(is_key_present(dictionary, "id"))
        check.is_true(is_key_present(dictionary, "managerId"))

        # Delete the group to avoid unnecessary data
        group.delete_group(auth, 200, response['created'][0]['id'])

    def test_04_get_groups_by_username_role(self, auth):
        group = GroupsApi()

        # Get groups by username and role
        response_data = group.get_groups_by_user_role(auth, 200, "gerardo.aragon", "ADMIN")

        # Validate if the response has cedulaId and student
        dictionary = response_data[0]
        check.is_true(is_key_present(dictionary, "name"))
        check.is_true(is_key_present(dictionary, "managerId"))

    def test_05_get_group_class_by_username(self, auth):
        group = GroupsApi()

        # Get groups by classes and username
        response_data = group.get_group_classes_by_username(auth, 200, "luis.ponce")

        # Validate if the response has cedulaId and student
        dictionary = response_data[0]
        check.is_true(is_key_present(dictionary, "id"))
        check.is_true(is_key_present(dictionary, "name"))

    def test_06_get_students_by_groups(self, auth):
        group = GroupsApi()

        # Search an existent group (Created previously by database)
        search_group = group.get_search_group(auth, 200, "7-1 (No eliminar)")
        group_id = search_group["data"][0]["id"]

        # Get all students
        response_data = group.get_students_by_group(auth, 200, group_id)

        # Validate if the response has cedulaId and student
        dictionary = response_data[0]
        check.is_true(is_key_present(dictionary, "id"))
        check.is_true(is_key_present(dictionary, "tutor"))

    def test_07_get_faults_by_group(self, auth):
        group = GroupsApi()

        # Search an existent group (Created previously by database)
        search_group = group.get_search_group(auth, 200, "7-1 (No eliminar)")
        group_id = search_group["data"][0]["id"]

        # Get all faults
        response_data = group.get_group_faults(auth, 200, group_id)

        # Validate if the response has .....
        dictionary = response_data["data"][0]
        check.is_true(is_key_present(dictionary, "id"))
        check.is_true(is_key_present(dictionary, "justification"))
        check.is_true(is_key_present(dictionary, "status"))
        check.equal(group_id, dictionary["groupId"])

    def test_08_get_group_by_id(self, auth):
        group = GroupsApi()

        # Create group if there are no groups
        group_name = group_name = "Sección " + (create_random_fields()[-5:])
        response_data = group.post_create_groups(auth, 201, group_name)
        group_id = response_data["created"][0]["id"]

        # Get group by id
        group_data = group.get_group_by_id(auth, 200, group_id)

        # Validate if the response has cedulaId and student
        check.is_true(is_key_present(group_data, "id"))
        check.is_true(is_key_present(group_data, "name"))
        check.is_true(is_key_present(group_data, "managerId"))

        # Delete the group to avoid unnecessary data
        group.delete_group(auth, 200, group_id)

    def test_09_edit_group(self, auth):
        group = GroupsApi()

        # Create group if there are no groups
        group_name = "Sección " + (create_random_fields()[-5:])
        response_data = group.post_create_groups(auth, 201, group_name)
        group_id = response_data["created"][0]["id"]

        # Edit group
        new_group_name = "edited_" + (create_random_fields()[-5:])
        group_data = group.put_edit_group(auth, 200, group_id, new_group_name)

        # Validate if the response has .....
        payload = set_edit_group_payload(new_group_name)
        check.equal(new_group_name, group_data["name"])
        check.equal(payload["managerId"], group_data["managerId"])

        # Delete the group to avoid unnecessary data
        group.delete_group(auth, 200, group_id)

    def test_10_delete_group(self, auth):
        group = GroupsApi()

        # Create group if there are no groups
        group_name = "Sección " + (create_random_fields()[-5:])
        response_data = group.post_create_groups(auth, 201, group_name)
        group_id = response_data["created"][0]["id"]

        # Get all faults
        response_data = group.delete_group(auth, 200, group_id)

        # Verify if the response body contains...
        check.is_true(is_key_present(response_data, "id"))
        check.equal(int(group_id), int(response_data["id"]))
