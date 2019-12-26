from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('accounts:create')
TOKEN_URL = reverse('accounts:token')

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """ Test the accounts API"""

    def setUp(self):
        self.client = APIClient()
    
    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""

        payload = {
            'email':"test@gmail.com",
            'password': 'testpass',
            'display_name': 'Test name'
        }

        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('testpass',res.data)

    def test_user_exists(self):
        """Test creating a user that already exists fails"""
        payload = {
            'email':"test@gmail.com",
            'password': "testpassword",
            'display_name':"test user"
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        payload = {
            "email":"test@gmail.com",
            "password":"p4Ss",
        }
        res = self.client.post(CREATE_USER_URL,payload)
        
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload["email"]
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {
            "email": "test@gmail.com",
            "password":"TestP4ssW0rd"
        }
        create_user(**payload)
        res = self.client.post(TOKEN_URL,payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_create_token_invalid_credentials(self):
        """Test taht a token is not created invalid credentials"""
        create_user(email="test@gmail.com", password="testP4ssw0rd")
        payload = {'email':"test@gmail.com","password":"invalidpassword"}
        res = self.client.post(TOKEN_URL,payload)

        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token',res.data)

    def test_create_token_for_no_user(self):
        """Test that a token is not created if user does not exist."""
        payload = {'email':"test@gmail.com",'password':"P4ssw0rd"}
        res = self.client.post(TOKEN_URL,payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token',res.data)

    def test_create_token_missing_field(self):
        """Test that either email or passowrd is missing"""
        payload = {'email':'aaa', 'password':''}
        res = self.client.post(TOKEN_URL,payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)



