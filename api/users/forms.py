from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import APIUser


class APIUserCreationForm(UserCreationForm):
    class Meta:
        model = APIUser
        fields = ("email", "username")


class APIUserChangeForm(UserChangeForm):
    class Meta:
        model = APIUser
        fields = ("email", "username")
