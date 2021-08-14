from django.test import TestCase
from django.contrib.auth.hashers import check_password
from ..models import APIUser

# Create your tests here.


class APIUserTestCase(TestCase):
    """Test APIUser Model Functionalities"""

    def setUp(self) -> None:
        pass

    def test_user_creation_requires_username(self):
        """test username is required for user creation"""
        with self.assertRaises(ValueError) as e:
            APIUser.objects.create_user(
                username="", password="password1234", email="email@domain.com"
            )
        self.assertEqual(e.exception.args[0], "username must be set")

    def test_user_creation_requires_password(self):
        """test password is required for user creation"""
        with self.assertRaises(ValueError) as e:
            APIUser.objects.create_user(
                username="username", email="email@domain.com", password=""
            )
        self.assertEqual(e.exception.args[0], "password must be set")

    def test_user_creation_requires_email(self):
        """test email is required for user creation"""
        with self.assertRaises(ValueError) as e:
            APIUser.objects.create_user(
                username="username", password="password1234", email=""
            )
        self.assertEqual(e.exception.args[0], "email must be set")

    def test_can_create_user(self):
        """test user creation with all right paramters"""
        new_user = APIUser.objects.create_user(
            username="username", password="password", email="email@domain.com"
        )
        self.assertEqual(new_user.username, "username")
        self.assertEqual(new_user.email, "email@domain.com")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")
        self.assertNotEqual(new_user.password, "password")
        self.assertTrue(check_password("password", new_user.password))
        self.assertTrue(new_user.is_active)
        self.assertFalse(new_user.is_staff)
        self.assertFalse(new_user.is_superuser)

    def test_can_create_superuser(self):
        """test superuser creation with all right paramters"""
        new_user = APIUser.objects.create_superuser(
            username="super_username",
            password="password",
            email="email@super_domain.com",
        )
        self.assertEqual(new_user.username, "super_username")
        self.assertEqual(new_user.email, "email@super_domain.com")
        self.assertNotEqual(new_user.password, "password")
        self.assertTrue(check_password("password", new_user.password))
        self.assertTrue(new_user.is_active)
        self.assertTrue(new_user.is_staff)
        self.assertTrue(new_user.is_superuser)
