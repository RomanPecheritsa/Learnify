from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("learning/", include("lms.urls", namespace="learning")),
    path("users/", include("users.urls", namespace="users")),
]
