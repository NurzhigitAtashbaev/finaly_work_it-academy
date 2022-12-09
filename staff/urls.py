from django.urls import path

from .views import StaffListAPIView, ContactsListAPIView


urlpatterns = [
    path('list/', StaffListAPIView.as_view(), name='staff-list'),
    path('contacts/', ContactsListAPIView.as_view(), name='staff-contacts-list'),
]
