""" Users URL Configuration
"""

from django.urls import path, include
from .views import (
    ResendEmailVerificationView,
    VerifyEmailView,
    VerifyEmailViewGet,
)

urlpatterns = [
    path(
        r"registration/account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),  # to overwrite the account_email_verification_sent as stated here: https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html#registration
    path(
        "registration/resend-email/",
        ResendEmailVerificationView.as_view(),
        name="rest_resend_email",
    ),  # fixes #1 (Resend Email with non-existant email return 500)
    path(
        r"registration/account-confirm-email/<str:key>/",
        VerifyEmailViewGet.as_view(),
        name="account_email_verification_confirmation",
    ),
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
]
