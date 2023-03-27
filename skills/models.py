from django.db import models
from taggit.managers import TaggableManager


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.name
