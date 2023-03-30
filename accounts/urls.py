from django.urls import path

from .views import CustomUserDetail, CustomUserList, SocialLinkDetail, SocialLinkList

urlpatterns = [
    path("users/", CustomUserList.as_view(), name="customuser_list"),
    path("users/<int:pk>/", CustomUserDetail.as_view(), name="customuser_detail"),
    path("social-links/", SocialLinkList.as_view(), name="sociallink_list"),
    path(
        "social-links/<int:pk>/", SocialLinkDetail.as_view(), name="sociallink_detail"
    ),
]
