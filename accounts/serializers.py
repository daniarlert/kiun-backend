from rest_framework import serializers

from .models import CustomUser, SocialLink


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "name",
            "contact_email",
            "about",
        )


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = (
            "id",
            "name",
            "url",
        )
