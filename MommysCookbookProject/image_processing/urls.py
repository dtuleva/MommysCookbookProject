from django.urls import path

from MommysCookbookProject.image_processing import views

urlpatterns = [

    path("<str:recipe_slug>/", views.image_process, name="image_process"),

]
