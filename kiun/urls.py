from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/accounts/", include("accounts.urls")),
    path("api/v1/projects/", include("projects.urls")),
    path("api/v1/skills/", include("skills.urls")),
    path("api/v1/studies/", include("studies.urls")),
]
