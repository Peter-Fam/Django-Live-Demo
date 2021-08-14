from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.exceptions import ErrorDetail
from ..views import VerifyEmailViewGet


class EmailVerificationTestCase(TestCase):
    """Test Email Verification Functionalities"""

    def test_user_regisration_requires_email(self):
        """test user requires email on registration"""

        url = reverse("rest_register")
        c = APIClient()
        response = c.post(
            url,
            {
                "email": "",
                "password1": "password1234!@#",
                "password2": "password1234!@#",
            },
        )
        self.assertEqual(400, response.status_code)
        self.assertEqual(
            {"email": [ErrorDetail("This field may not be blank.", code="blank")]},
            response.data,
        )

    def test_user_login_requires_verified_email(self):
        """test user requires verifing email to login"""
        url = reverse("rest_register")
        c = APIClient()
        response = c.post(
            url,
            {
                "email": "test@example.com",
                "password1": "password1234!@#",
                "password2": "password1234!@#",
            },
            format="json",
        )
        self.assertEqual(201, response.status_code)
        self.assertEqual({"detail": "Verification e-mail sent."}, response.data)
        login_url = reverse("rest_login")
        login_reponse = c.post(
            login_url, {"email": "test@example.com", "password": "password1234!@#"}
        )
        self.assertEqual(400, login_reponse.status_code)
        self.assertEqual(
            {
                "non_field_errors": [
                    ErrorDetail("E-mail is not verified.", code="invalid")
                ]
            },
            login_reponse.data,
        )
