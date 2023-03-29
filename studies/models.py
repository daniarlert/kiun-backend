from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Achievement(models.Model):
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def clean(self):
        super.clean()
        if self.end_date and self.start_date and self.start_date > self.end_date:
            raise ValidationError(_("End date must be greater than start date"))

    class Meta:
        abstract = True


class Titulation(Achievement):
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)

    def __str__(self):
        return self.degree


class Certification(Achievement):
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)

    def __str__(self):
        return self.title
