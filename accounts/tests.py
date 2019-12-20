from django.test import TestCase
from django.contrib.auth import get_user_model

import accounts.models


class ModelTest(TestCase):

    def test_create_user_with_an_email_is_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@gmail.com'
        password = "T3stP4ssw0rd"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email,email)
        self.assertEqual(user.check_password(password))