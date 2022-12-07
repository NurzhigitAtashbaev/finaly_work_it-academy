from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import TourSerializer, CertificateSerializer
from .models import OrderCertificate
from travel.models import Tour


class OrderCreateView(generics.ListCreateAPIView):
    queryset = OrderCertificate.objects.all()
    serializer_class = CertificateSerializer


@receiver(post_save, sender=OrderCertificate)
def create_profile(sender, instance: OrderCertificate, created, **kwargs):
    print(OrderCreateView)
    if created:
        send_mail('Contact Form',
                  f'{instance.info}'
                  f'Сертификат на Тур:{instance.tours},'
                  f'стоимость {instance.tours.price} сом',
                  settings.EMAIL_HOST_USER,
                  [f'{instance.email}'],
                  fail_silently=False)


