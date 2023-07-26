from django.urls import path

from MommysCookbookProject.user_auth.views import UserRegisterView, UserLoginView, UserListView, \
    UserLogoutConfirmationView, UserLogoutView, UserDetailsView, UserUpdateView, UserDeleteView, UserPasswordChangeView, \
    UserPasswordChangeSuccessView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user_register"),
    path("login/", UserLoginView.as_view(), name="user_login"),
    path("logout_confirm/", UserLogoutConfirmationView.as_view(), name="user_logout_confirm"),
    path("logout/", UserLogoutView.as_view(), name="user_logout"),
    path("profile/", UserDetailsView.as_view(), name="user_details"),
    path("edit_profile/", UserUpdateView.as_view(), name="user_edit"),
    path("delete_profile/", UserDeleteView.as_view(), name="user_delete"),
    path("change_password/", UserPasswordChangeView.as_view(),name="user_change_password"),
    path("change_password_success/", UserPasswordChangeSuccessView.as_view(), name="user_change_password_success"),
    path("3F61F6AA593BCEAA/", UserListView.as_view(), name="user_list"),  # xxh64 hash for "user_list",

]
