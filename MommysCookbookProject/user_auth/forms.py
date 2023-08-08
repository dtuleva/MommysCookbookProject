from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from MommysCookbookProject.user_auth.models import CookbookUser


class CookbookUserRegisterForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")


class CookbookLoginForm(auth_forms.AuthenticationForm):
        class Meta(auth_forms.UserCreationForm.Meta):
            model = get_user_model()
            fields = ("username", "email")


class ProfilePictureUpdate(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("profile_picture",)
        widgets = {
            "profile_picture": forms.FileInput()
        }