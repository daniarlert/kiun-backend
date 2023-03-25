from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, SocialLink


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "name", "contact_email", "is_staff", "is_active"]
    list_filter = ["email", "name", "contact_email", "is_staff", "is_active"]
    fieldsets = (
        (None, {"fields": ("email", "name", "contact_email", "about", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "contact_email",
                    "about",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ["email", "name", "contact_email"]
    ordering = ["email", "name", "contact_email"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SocialLink)
