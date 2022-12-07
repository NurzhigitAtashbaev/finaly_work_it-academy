from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from attractions.models import Attractions


class CategoryTest(TestCase):

    def setUp(self, **product_data):

        category_data = {
            'title': 'title',
            'description': 'title',
        }
        category = Attractions.objects.create(**category_data)

    def test_category_list(self):
        url = reverse('attractions')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_category_detail(self):
        category = Attractions.objects.first()
        url = reverse('attractions-detail', args=(category.pk,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_category_create(self):
        url = reverse('attractions-create')
        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)
