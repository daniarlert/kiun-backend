from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from .models import Skill


class SkillSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Skill
        fields = (
            "id",
            "name",
            "description",
            "tags",
        )
