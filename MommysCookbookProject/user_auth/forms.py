from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model


class CookbookUserRegisterForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")


class CookbookLoginForm(auth_forms.AuthenticationForm):
    # username = auth_forms.UsernameField(
    #     widget=forms.TextInput(attrs={
    #         "autofocus": True,
    #         "placeholder": "Username"
    #     })
    # )
    #
    # password = forms.CharField(
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={
    #         "autocomplete": "current-password",
    #         "placeholder": "Password"
    #     })
    # )
        class Meta(auth_forms.UserCreationForm.Meta):
            model = get_user_model()
            fields = ("username", "email")
