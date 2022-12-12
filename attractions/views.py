from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Attractions
from .serializers import AttractionsSerializer, AttractionsUpdateSerializer, AttractionsDestroySerializer


class AttractionsListAPIView(generics.ListAPIView):
    """Список Достопримечательностей"""
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer


class AttractionsCreateAPIView(generics.ListCreateAPIView):
    """Создание Достопримечательностей"""
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer
    permission_classes = [IsAdminUser]


class AttractionsRetrieveAPIView(generics.RetrieveAPIView):
    """Детальный просмотр Достопримечательностей"""
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer


class AttractionsUpdateAPIView(generics.UpdateAPIView):
    """Изменение-Обновление Достопримечательностей,Доступ только у администратора"""
    queryset = Attractions.objects.all()
    serializer_class = AttractionsUpdateSerializer
    permission_classes = [IsAdminUser]


class AttractionsDestroyAPIView(generics.DestroyAPIView):
    """Удаление Достопримечательностей, удалять может только Администратора"""
    queryset = Attractions.objects.all()
    serializer_class = AttractionsDestroySerializer
    permission_classes = [IsAdminUser]