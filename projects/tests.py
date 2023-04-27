import django_perf_rec
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .models import Project


class ProjectTests(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test project",
            short_description="Test project short description",
            url="https://example.com",
            image=SimpleUploadedFile(
                name="test_image.jpg",
                content=b"some content",
                content_type="image/jpeg",
            ),
            long_description="Test project long description",
        )

    def test_project_creation(self):
        project = Project.objects.get(title="Test project")

        self.assertIsNotNone(project)
        self.assertEqual(project.short_description, "Test project short description")
        self.assertEqual(project.url, "https://example.com")
        self.assertEqual(project.long_description, "Test project long description")

    def test_project_deletion(self):
        project = Project.objects.get(title="Test project")
        project.delete()

        self.assertFalse(Project.objects.filter(title="Test project").exists())

    def test_project_str(self):
        project = Project.objects.get(title="Test project")

        self.assertEqual(str(project), "Test project")

    def test_project_image_upload(self):
        # TODO:
        pass

    def test_project_tags(self):
        project = Project.objects.get(title="Test project")
        project.tags.add("test1", "test2")

        project_tags = project.tags.all()

        self.assertEqual(project_tags.count(), 2)
        self.assertIn("test1", project_tags.values_list("name", flat=True))
        self.assertIn("test2", project_tags.values_list("name", flat=True))

    def test_project_performance(self):
        with django_perf_rec.record():
            list(Project.objects.all())
