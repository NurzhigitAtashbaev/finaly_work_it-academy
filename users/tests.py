# from django.test import TestCase
# from django.urls import reverse
#
# from rest_framework.test import APIClient
#
# from .models import CustomUser
# from .serializers import UsersProfileSerializer
#
#
# class TestUserAPI(TestCase):
#     def setUp(self):
#         # Set up test data
#         self.client = APIClient()
#         self.user = CustomUser.objects.create(username="testuser", email="test@example.com")
#
#     def test_get_users(self):
#         # Test if GET request to the /users/ endpoint returns a list of users
#         response = self.client.get(reverse("user-list"))
#         users = CustomUser.objects.all()
#         serializer = UsersProfileSerializer(users, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, 200)
#
#     def test_get_user_details(self):
#         # Test if GET request to the /users/<id>/ endpoint returns the details of a user
#         response = self.client.get(reverse("user-detail", kwargs={"pk": self.user.id}))
#         user = CustomUser.objects.get(pk=self.user.id)
#         serializer = UsersProfileSerializer(user)
#
