from rest_framework import generics

from .models import AboutStaff, Contacts
from .serializers import StaffListSerializer

class StaffListAPIView(generics.ListAPIView):
    """Список сотрудников """
    queryset = AboutStaff.objects.all()
    serializer_class = StaffListSerializer