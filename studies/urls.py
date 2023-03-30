from django.urls import path

from .views import (
    CertificationDetail,
    CertificationList,
    TitulationDetail,
    TitulationList,
)

urlpatterns = [
    path("titulation/", TitulationList.as_view(), name="titulation_list"),
    path("titulation/<int:pk>/", TitulationDetail.as_view(), name="titulation_detail"),
    path("certification/", CertificationList.as_view(), name="certification_list"),
    path(
        "certification/<int:pk>/",
        CertificationDetail.as_view(),
        name="certification_detail",
    ),
]
