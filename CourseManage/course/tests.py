from rest_framework.test import APITestCase, RequestsClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserLoginSignupTest(APITestCase, RequestsClient):

    def test_signup(self):
        user_data = {"username": "Sam", "password": "sam123asd", "email": "sam@gmail.com"}
        response = self.client.post("/api/v1/users/", user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().username, "Sam")
        self.assertEqual(User.objects.get().email, "sam@gmail.com")


    def test_login(self):
        user_data = {"username": "Sam", "password": "sam123asd", "email": "sam@gmail.com"}
        self.client.post("/api/v1/users/", user_data, format="json")
        response = self.client.post("/api/v1/token/login/", user_data, format="json")
        self.client.credentials(HTTP_AUTHORIZATION="Token"+response.data["auth_token"])
        self.assertTrue(response.data["auth_token"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = Token.objects.get(user__username="Sam")
        self.assertEqual(token.key, response.data["auth_token"])

class TestAPIPoint(APITestCase):

    def testAddCourse(self):
        user_data = {"username": "Sam", "password": "sam123asd", "email": "sam@gmail.com"}
        self.client.post("/api/v1/users/", user_data, format="json")
        token = self.client.post("/api/v1/token/login/", user_data, format="json")
        self.client.credentials(HTTP_AUTHORIZATION="Token" + token.data["auth_token"])
        courses = [{"name": "cs100", "credit": 2, "student": user_data["username"]},
                   {"name": "cs200", "credit": 3, "student": user_data["username"]},
                   {"name": "cs300", "credit": 4, "student": user_data["username"]}]
        for course in courses:
            response = self.client.post("/api/v1/course/add/", course, format="json")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data["name"], course["name"])
            self.assertEqual(response.data["credit"], course["credit"])
            self.assertEqual(response.data["student"], course["student"])

    def testGetAndGetAllCourse(self):
        user_data = {"username": "Sam", "password": "sam123asd", "email": "sam@gmail.com"}
        self.client.post("/api/v1/users/", user_data, format="json")
        token = self.client.post("/api/v1/token/login/", user_data, format="json")
        self.client.credentials(HTTP_AUTHORIZATION="Token" + token.data["auth_token"])
        courses = [{"name": "cs100", "credit": 2, "student": user_data["username"]},
                   {"name": "cs200", "credit": 3, "student": user_data["username"]},
                   {"name": "cs300", "credit": 4, "student": user_data["username"]}]
        for course in courses:
            self.client.post("/api/v1/course/add/", course, format="json")
        response_all = self.client.get("/api/v1/course/")
        self.assertEqual(len(response_all.data), 3)
        response_1 = self.client.get("/api/v1/course/cs100/")
        self.assertEqual(response_1.data["name"], "cs100")
        self.assertEqual(response_1.data["credit"], 2)
        self.assertEqual(response_1.data["student"], "Sam")

    def testUpdateCourse(self):
        user_data = {"username": "Sam", "password": "sam123asd", "email": "sam@gmail.com"}
        self.client.post("/api/v1/users/", user_data, format="json")
        token = self.client.post("/api/v1/token/login/", user_data, format="json")
        self.client.credentials(HTTP_AUTHORIZATION="Token" + token.data["auth_token"])
        courses = [{"name": "cs100", "credit": 2, "student": user_data["username"]},
                   {"name": "cs200", "credit": 3, "student": user_data["username"]},
                   {"name": "cs300", "credit": 4, "student": user_data["username"]}]
        for course in courses:
            self.client.post("/api/v1/course/add/", course, format="json")
        update_data = {"name": "cs100", "credit": 10}
        self.client.post("/api/v1/course/update/cs100/", update_data, format="json")
        new_course = self.client.get("/api/v1/course/cs100/")
        self.assertEqual(new_course.data["credit"], 10)

    def testDeleteCourse(self):
        user_data = {"username": "Sam", "password": "sam123asd", "email": "sam@gmail.com"}
        self.client.post("/api/v1/users/", user_data, format="json")
        token = self.client.post("/api/v1/token/login/", user_data, format="json")
        self.client.credentials(HTTP_AUTHORIZATION="Token" + token.data["auth_token"])
        courses = [{"name": "cs100", "credit": 2, "student": user_data["username"]},
                   {"name": "cs200", "credit": 3, "student": user_data["username"]},
                   {"name": "cs300", "credit": 4, "student": user_data["username"]}]
        for course in courses:
            self.client.post("/api/v1/course/add/", course, format="json")
        self.client.delete("/api/v1/course/delete/cs100/")
        courses = self.client.get("/api/v1/course/")
        self.assertEqual(len(courses.data), 2)