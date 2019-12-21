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
    
    def test_new_user_invalid_email(self):
        """Test the email for a new user is normalized"""

        email = "test@GMAIL.com"
        user = get_user_model().objects.create(email,"test123")
        self.assertEqual(user.email, email.lower())
    
    def test_create_new_superuser(self):
        """Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)