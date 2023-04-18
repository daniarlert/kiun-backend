from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from taggit.managers import TaggableManager


class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    url = models.URLField()
    image = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to="projects"
    )
    long_description = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.title
