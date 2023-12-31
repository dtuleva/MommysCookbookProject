from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import mixins as auth_mixins

from django.urls import reverse_lazy
from django.views import generic as views

from MommysCookbookProject.user_auth.forms import CookbookUserRegisterForm, CookbookLoginForm, ProfilePictureUpdate


class UserRegisterView(views.CreateView):

    template_name = "user_auth/user_register.html"
    form_class = CookbookUserRegisterForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):  # todo: username or pass invalid message, redirect already logged
    template_name = "user_auth/user_login.html"
    form_class = CookbookLoginForm
    redirect_authenticated_user = False


class UserLogoutConfirmationView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = "user_auth/user_logout.html"


class UserLogoutView(auth_views.LogoutView):
    """
         Logs current user out and redirects to UserLoginView
    """


# todo: change mixin to PermissionRequired
class CurrentUserMixin(auth_mixins.LoginRequiredMixin):
    """
         Mixin to get the current logged-in user as the object for Detail, Update and Delete Views.
    """

    def get_object(self, queryset=None):
        user = self.request.user
        if user.is_authenticated:
            return user


class UserDetailsView(CurrentUserMixin, views.DetailView):
    model = get_user_model()
    template_name = "user_auth/user_details.html"


class UserUpdateView(CurrentUserMixin, views.UpdateView):
    model = get_user_model()
    template_name = 'user_auth/user_edit.html'
    fields = ['username', 'email', 'screen_name']
    success_url = reverse_lazy('user_details')


class UserDeleteView(CurrentUserMixin, views.DeleteView):
    model = get_user_model()
    template_name = "user_auth/user_delete.html"
    success_url = reverse_lazy("index")


class UserPasswordChangeView(auth_views.PasswordChangeView):
    template_name = "user_auth/user_change_password.html"
    success_url = reverse_lazy("user_change_password_success")


class UserPasswordChangeSuccessView(views.TemplateView):
    template_name = "user_auth/user_change_password_success.html"


class UserListView(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = "user_auth/user_list.html"
    model = get_user_model()


class UserPictureChangeView(CurrentUserMixin, views.UpdateView):
    template_name = "user_auth/user_change_picture.html"
    form_class = ProfilePictureUpdate
    model = get_user_model()
    success_url = reverse_lazy('user_details')
