from django.urls import path

from MommysCookbookProject.home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("favorites_update/<str:slug>/", views.favorite_functionality, name='favorites_update'),
    path("note_create/<str:slug>/", views.note_create, name='note_create'),
    path("note_edit/<int:note_pk>/", views.note_edit, name='note_edit'),
    path("note_delete/<int:note_pk>/", views.note_delete, name='note_delete'),

]