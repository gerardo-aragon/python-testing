import json
import time

from utils.api_helper import *
from src.endpoints.auth.auth import *
from src.endpoints.courses.courses import *
from utils.asserts import *
from pytest_check import check
from utils.payloads.create_course import *


@pytest.mark.usefixtures("auth")
class TestCourseApi:

    def test_01_create_course_successful(self, auth):
        course = CoursesApi()

        # Create course
        response_data = course.post_create_courses(auth, 201, "Español")

        # verify if data is present...
        dictionary = response_data['created'][0]
        check.is_true(is_key_present(dictionary, "name"))
        check.is_true(is_key_present(dictionary, "teachers"))


    def test_02_get_courses(self, auth):
        course = CoursesApi()
        
        # get all courses
        response_data = course.get_all_courses(auth, 200)

        # Verify if data is present
        dictionary = response_data[0]
        check.is_true(is_key_present(dictionary, "id"))
        check.is_true(is_key_present(dictionary, "name"))


    def test_03_get_courses_view(self, auth):
        course = CoursesApi()

        # get courses view
        response_data = course.get_all_courses_view(auth, 200)

        # Verify if data is present
        dictionary = response_data["data"][0]
        check.is_true(is_key_present(dictionary, "courseName"))
        check.is_true(is_key_present(dictionary["teachers"][0], "id"))


    def test_04_get_course_by_id(self, auth):
        course = CoursesApi()

        # get course id
        courses = course.get_all_courses(auth, 200)
        course_id = courses[0]["id"]
        
        # get course by id
        dictionary = course.get_course_by_id(auth, 200, course_id)

        # Verify if data is present
        check.is_true(is_key_present(dictionary, "courseId"))
        check.is_true(is_key_present(dictionary, "courseName"))
    
    
    def test_05_edit_course(self, auth):
        course = CoursesApi()

        # get course id
        courses = course.get_all_courses(auth, 200)
        course_id = courses[0]["id"]
        
        # update course
        response_data = course.put_edit_course(auth, 200, course_id)

        # Verify if data is present
        dictionary = set_edit_course_payload()
        check.is_true(is_key_present(response_data, "name"))
        check.equal(response_data["teacherIds"][0], dictionary["teacherIds"][0])
        




