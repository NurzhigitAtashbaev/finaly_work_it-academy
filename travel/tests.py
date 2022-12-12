from django.test import TestCase
from rest_framework.reverse import reverse
from .models import Category, Types, Tour


class TravelModelTest(TestCase):
    def setUp(self):
        category_data = {
            "title": "Маковое поле"
        }
        category = Category.objects.create(**category_data)
        types_data = {
            "title": "type"
        }
        types = Types.objects.create(**types_data)

        tour_data = {
            "category": category,
            "types": types,
            "title": "tours title",
            "slug": "tours",
            "body": "body",
            "start_day": "2022-12-12",
            "end_day": "2022-12-12",
            "quantity_of_seats": 1

        }
        tour = Tour.objects.create(**tour_data)

    def test_travel(self):
        url = reverse('tour-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_tour_detail(self, response=None):
        url = reverse('tour-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_data(self, response=None):
        url = reverse('tour-category', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



