from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("api/projects/", include("projects.urls")),
    path("api/skills/", include("skills.urls")),
    path("api/studies/", include("studies.urls")),
]
