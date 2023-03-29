from django.test import TestCase

from .models import Skill


class SkillsTests(TestCase):
    def setUp(self) -> None:
        self.skill = Skill.objects.create(
            name="Test skill",
            description="Test skill description",
        )

        self.skill.tags.add("test1", "test2")

    def test_skill_creation(self):
        skill = Skill.objects.get(name="Test skill")

        self.assertEqual(skill.description, "Test skill description")

    def test_skill_deletion(self):
        skill = Skill.objects.get(name="Test skill")
        skill.delete()

        self.assertFalse(Skill.objects.filter(name="Test skill").exists())

    def test_skill_str(self):
        skill = Skill.objects.get(name="Test skill")

        self.assertEqual(str(skill), "Test skill")

    def test_skill_tags(self):
        skill = Skill.objects.get(name="Test skill")

        skill_tags = skill.tags.all()

        self.assertEqual(skill_tags.count(), 2)
        self.assertIn("test1", skill_tags.values_list("name", flat=True))
        self.assertIn("test2", skill_tags.values_list("name", flat=True))
