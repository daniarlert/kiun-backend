from rest_framework import generics

from .models import CustomUser, SocialLink
from .serializers import CustomUserSerializer, SocialLinkSerializer


class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class SocialLinkList(generics.ListAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer


class SocialLinkDetail(generics.RetrieveAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
