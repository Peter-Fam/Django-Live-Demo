from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import APIUser
from .forms import APIUserCreationForm, APIUserChangeForm
from .models import APIUser


class APIUserAdmin(UserAdmin):
    add_form = APIUserCreationForm
    form = APIUserChangeForm
    model = APIUser
    list_display = (
        "email",
        "username",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "username",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email", "username")
    ordering = ("email",)


admin.site.register(APIUser, APIUserAdmin)
