from django.urls import path

from MommysCookbookProject.home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("favorites_update/<str:slug>/", views.favorite_functionality, name='favorites_update'),

]