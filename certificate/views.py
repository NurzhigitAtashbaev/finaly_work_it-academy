from django.shortcuts import render
from rest_framework import generics
from .serializers import CertificateSerializer
from .models import Certificate


class OrderCertificateView(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

