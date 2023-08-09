from django.contrib import admin
from django.contrib.auth import get_user_model
import django.contrib.auth.forms as auth_forms

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    form = auth_forms.UserChangeForm
    list_display = ("username", "email", "screen_name", "date_joined", "is_staff")
    search_fields = ("username", "email", "screen_name")
    list_filter = ("date_joined", "is_staff")
    readonly_fields = ("username", "email", "screen_name", "date_joined", "password")

