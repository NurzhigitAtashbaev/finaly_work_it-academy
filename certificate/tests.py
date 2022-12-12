from django.test import TestCase
from rest_framework.reverse import reverse
from certificate.models import OrderCertificate
from travel.models import Category, Types, Tour


class CertificateModelTest(TestCase):
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

        certificate_data = {
            "tours": tour,
            "info": "test",
            "count_people": 1,
            "email": "test@gmail.com",
            "phone": "+996700201399",
            "sender": "test",
            "addressee": "test"

        }
        certificate = OrderCertificate.objects.create(**certificate_data)

    def test_certificate_list(self):
        url = reverse('buy-certificate')
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)


