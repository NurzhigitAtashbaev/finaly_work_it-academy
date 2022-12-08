from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import generics
from .serializers import CertificateSerializer
from .models import OrderCertificate



class OrderCreateView(generics.ListCreateAPIView):
    """Покупка сертификата"""
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


