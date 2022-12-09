from django.conf import settings
from time import sleep
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import generics
from .serializers import CertificateSerializer
from .models import OrderCertificate
from .tasks import send_feedback_email_task


class OrderCreateView(generics.ListCreateAPIView):
    """Покупка сертификата"""
    queryset = OrderCertificate.objects.all()
    serializer_class = CertificateSerializer

    def send_email(self):
        send_feedback_email_task.apply_async(args=[
            self.cleaned_data["email"], self.cleaned_data["message"]
        ]
        )


# @receiver(post_save, sender=OrderCertificate)
# def send_certificate(sender, instance: OrderCertificate, created, **kwargs):
#     print(OrderCreateView)
#     if created:
#         send_mail('Contact Form',
#                   f'{instance.info}'
#                   f'Сертификат на Тур:{instance.tours},'
#                   f'стоимость {instance.tours.price} сом',
#                   settings.EMAIL_HOST_USER,
#                   [f'{instance.email}'],
#                   fail_silently=False)
