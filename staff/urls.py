from django.urls import path

from .views import StaffListAPIView


urlpatterns = [
    path('list/', StaffListAPIView.as_view(), name='staff-list')
]