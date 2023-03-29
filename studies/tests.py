from django.test import TestCase

from .models import Certification, Titulation


class TitulationTests(TestCase):
    def setUp(self) -> None:
        self.titulation = Titulation.objects.create(
            degree="Test degree",
            institution="Test institution",
            description="Test titulation description",
            start_date="2020-01-01",
            end_date="2020-01-02",
        )

    def test_titulation_creation(self):
        titulation = Titulation.objects.get(degree="Test degree")

        self.assertEqual(titulation.institution, "Test institution")
        self.assertEqual(titulation.description, "Test titulation description")
        self.assertEqual(titulation.start_date.strftime("%Y-%m-%d"), "2020-01-01")
        self.assertEqual(titulation.end_date.strftime("%Y-%m-%d"), "2020-01-02")

    def test_titulation_deletion(self):
        titulation = Titulation.objects.get(degree="Test degree")
        titulation.delete()

        self.assertFalse(Titulation.objects.filter(degree="Test degree").exists())

    def test_titulation_str(self):
        titulation = Titulation.objects.get(degree="Test degree")

        self.assertEqual(str(titulation), "Test degree")


class CertificationTests(TestCase):
    def setUp(self) -> None:
        self.certification = Certification.objects.create(
            title="Test certification",
            organization="Test organization",
            description="Test certification description",
            start_date="2020-01-01",
            end_date="2020-01-02",
        )

    def test_certification_creation(self):
        certification = Certification.objects.get(title="Test certification")

        self.assertEqual(certification.organization, "Test organization")
        self.assertEqual(certification.description, "Test certification description")
        self.assertEqual(certification.start_date.strftime("%Y-%m-%d"), "2020-01-01")
        self.assertEqual(certification.end_date.strftime("%Y-%m-%d"), "2020-01-02")

    def test_certification_deletion(self):
        certification = Certification.objects.get(title="Test certification")
        certification.delete()

        self.assertFalse(
            Certification.objects.filter(title="Test certification").exists()
        )

    def test_certification_str(self):
        certification = Certification.objects.get(title="Test certification")

        self.assertEqual(str(certification), "Test certification")
