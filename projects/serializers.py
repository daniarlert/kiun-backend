from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from .models import Project


class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "short_description",
            "url",
            "image",
            "long_description",
            "tags",
        )
