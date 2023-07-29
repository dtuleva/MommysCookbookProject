from django.contrib import admin
from django.contrib.auth import get_user_model
import django.contrib.auth.forms as auth_forms

UserModel = get_user_model()

#django.contrib.auth.admin.UserAdmin
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    form = auth_forms.UserChangeForm
