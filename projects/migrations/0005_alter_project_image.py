# Generated by Django 4.2 on 2023-04-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0004_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.FileField(upload_to=""),
        ),
    ]