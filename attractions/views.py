from rest_framework import generics

from .models import Attractions
from .serializers import AttractionsSerializer, AttractionsUpdateSerializer, AttractionsDestroySerializer


class AttractionsListAPIView(generics.ListAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer


class AttractionsCreateAPIView(generics.ListCreateAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer


class AttractionsUpdateAPIView(generics.UpdateAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsUpdateSerializer


class AttractionsRetrieveAPIView(generics.DestroyAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsDestroySerializer
