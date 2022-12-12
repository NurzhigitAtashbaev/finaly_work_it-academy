import uuid
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from .models import Category, Types, Tour, Entry
from users.models import CustomUser


class TravelModelTest(TestCase):
    def setUp(self):
        username = 'user_{}'.format(uuid.uuid4().hex)
        email = 'email_{}'.format(uuid.uuid4().hex)

        self.user = CustomUser(username=username, email=email)
        self.user.set_password('user')
        self.user.save()

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

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

        user_data = {
            "email": "user@gmail.com",
            "phone": "+996700112233",
            "birth_date": "2001-01-12",
            "is_active": True
        }
        user = CustomUser.objects.create(**user_data)

        entry_data = {
            "user": user,
            "tour": tour,
            "date_buy": "2022-12-13"
        }
        entry = Entry.objects.create(**entry_data)

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

    def test_entry(self):
        url = reverse('tour-entry')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form id="entry-form"')


