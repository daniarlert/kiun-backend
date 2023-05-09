# Generated by Django 4.2 on 2023-04-14 16:40

import pathlib

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.FileField(
                storage=django.core.files.storage.FileSystemStorage(
                    location=pathlib.PurePosixPath("/app/media")
                ),
                upload_to="projects",
            ),
        ),
    ]