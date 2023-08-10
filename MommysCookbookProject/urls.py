from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("MommysCookbookProject.home.urls")),
    path("recipes/", include("MommysCookbookProject.recipe.urls")),
    path("", include("MommysCookbookProject.user_auth.urls")),
    path("conversion/", include("MommysCookbookProject.conversion.urls")),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
