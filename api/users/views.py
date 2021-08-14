from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from dj_rest_auth.registration.views import VerifyEmailView


class VerifyEmailViewGet(VerifyEmailView):
    """Email Verification API Point"""

    def get(self, *args, **kwargs):
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        return Response({"detail": "ok"}, status=status.HTTP_200_OK)
