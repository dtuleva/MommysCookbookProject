from django.urls import path

from MommysCookbookProject.conversion import views

urlpatterns = [
    path("", views.convert_measurement, name="convert"),
    path("copy-convertion-result/", views.copy_conversion_result, name="copy_convertion_result")


]