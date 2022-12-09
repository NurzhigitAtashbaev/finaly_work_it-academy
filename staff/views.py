from rest_framework import generics
from .models import AboutStaff, Contacts
from .serializers import StaffListSerializer, ContactSerializer


class StaffListAPIView(generics.ListAPIView):
    """Список сотрудников """
    queryset = AboutStaff.objects.all()
    serializer_class = StaffListSerializer


class ContactsListAPIView(generics.ListAPIView):
    """Список Контактов"""
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer
