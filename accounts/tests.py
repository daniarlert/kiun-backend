from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import CustomUser, SocialLink


class UsersTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email="john@doe.com",
            password="testpass123",
            name="John Doe",
            contact_email="johncontact@doe.com",
            about="John Doe is real.",
        )

    def test_user_creation(self):
        user = CustomUser.objects.get(email="john@doe.com")

        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.contact_email, "johncontact@doe.com")
        self.assertEqual(user.about, "John Doe is real.")

    def test_user_deletion(self):
        user = CustomUser.objects.get(email="john@doe.com")
        user.delete()

        self.assertFalse(CustomUser.objects.filter(email="john@doe.com").exists())

    def test_user_str(self):
        user = CustomUser.objects.get(email="john@doe.com")

        self.assertEqual(str(user), "john@doe.com")


class SocialLinkTests(TestCase):
    def setUp(self):
        self.social_link = SocialLink.objects.create(
            name="Test social link",
            url="https://test.com",
        )

    def test_social_link_creation(self):
        social_link = SocialLink.objects.get(name="Test social link")

        self.assertEqual(social_link.url, "https://test.com")

    def test_social_link_deletion(self):
        social_link = SocialLink.objects.get(name="Test social link")
        social_link.delete()

        self.assertFalse(SocialLink.objects.filter(name="Test social link").exists())

    def test_social_link_str(self):
        social_link = SocialLink.objects.get(name="Test social link")

        self.assertEqual(str(social_link), "Test social link")
