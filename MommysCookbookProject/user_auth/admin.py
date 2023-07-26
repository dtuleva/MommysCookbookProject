from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    # list_display = ("pk", "username", "email") - hides built-in sugar
    pass


