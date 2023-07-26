from django.urls import path

from MommysCookbookProject.home import views


urlpatterns = [
    path("", views.index, name="index"),
]