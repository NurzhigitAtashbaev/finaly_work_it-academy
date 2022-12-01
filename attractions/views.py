from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Attractions
from .serializers import AttractionsSerializer, AttractionsUpdateSerializer, AttractionsDestroySerializer


# Список Достопримечательностей
class AttractionsListAPIView(generics.ListAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer


# Создание Достопримечательностей
class AttractionsCreateAPIView(generics.ListCreateAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer
    permission_classes = [IsAdminUser]


# Детальный просмотр Достопримечательностей
class AttractionsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer


# Изменение-Обновление Достопримечательностей
class AttractionsUpdateAPIView(generics.UpdateAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsUpdateSerializer
    permission_classes = [IsAdminUser]


# Удаление Достопримечательностей, удалять может только Админ
class AttractionsDestroyAPIView(generics.DestroyAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsDestroySerializer
    permission_classes = [IsAdminUser]
