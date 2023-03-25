from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    url = models.URLField()
    image = models.ImageField(upload_to="media/projects")
    long_description = models.TextField()

    def __str__(self):
        return self.title
