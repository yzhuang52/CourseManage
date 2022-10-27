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
