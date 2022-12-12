from django.contrib.auth import authenticate
from django.test import TestCase
from rest_framework.reverse import reverse
from django.urls import reverse
from rest_framework.test import APIClient
from .models import CustomUser, UserProfile


class CustomUserTest(TestCase):
    def setUp(self) -> None:
        custom_user_data = {
            'username': "username",
            'email': "username@gmail.com",
            'phone': '+9960700998888',
            'is_active': True,
        }
        user = CustomUser.objects.create(**custom_user_data)

    def test_user_register(self):
        url = reverse('user-register')
        response = self.client.post(url, data={
            'username': "username",
            'email': "username@gmail.com",
            'phone': '+9960700998888'
        })

        self.assertEqual(response.status_code, 200)


class CustomUserTestCase(TestCase):
    """тест на смену пароля """
    def test_change_password(self):
        user = CustomUser.objects.create_user(username="testuser", email="testuser@gmail.com",
                                              password="testpassword", phone="+996700979797")

        client = APIClient()
        client.force_authenticate(user=user)
        user.is_active = True
        user.save()

        url = reverse('change-password')
        response = client.put(url, data={
            'old_password': "testpassword",
            'new_password': "newpassword",
        })

        self.assertEqual(response.status_code, 200)

        authenticated_user = authenticate(email="testuser@gmail.com", password="newpassword")
        self.assertTrue(authenticated_user)
