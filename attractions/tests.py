from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Attractions


class AttractionsModelTest(TestCase):
    def setUp(self):
        self.attraction = Attractions.objects.create(
            title="Иссы-Куль",
            description="Иссы-Куль озеро кыргызстана для отдыха"
        )

    def test_attraction_creation(self):
        self.assertTrue(isinstance(self.attraction, Attractions))
        self.assertEqual(self.attraction.__str__(), self.attraction.title)
        self.assertEqual(self.attraction.title, "Иссы-Куль")
        self.assertEqual(self.attraction.description, "Иссы-Куль озеро кыргызстана для отдыха")

