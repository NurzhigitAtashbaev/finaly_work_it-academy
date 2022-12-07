from django.urls import path

<<<<<<< HEAD
from .views import StaffListAPIView, ContactsListAPIView


urlpatterns = [
    path('list/', StaffListAPIView.as_view(), name='staff-list'),
    path('contacts/', ContactsListAPIView.as_view(), name='staff-contacts-list'),
]
=======
from .views import StaffListAPIView


urlpatterns = [
    path('list/', StaffListAPIView.as_view(), name='staff-list')
]
>>>>>>> cceb02a (cleaning + staff view, serializers,urls)
