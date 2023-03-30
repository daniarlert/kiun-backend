from rest_framework import serializers

from .models import Certification, Titulation


class TitulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulation
        fields = (
            "id",
            "degree",
            "institution",
            "description",
            "start_date",
            "end_date",
        )


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = (
            "id",
            "title",
            "organization",
            "description",
            "start_date",
            "end_date",
        )
