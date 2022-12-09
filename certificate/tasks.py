from time import sleep

from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task
from django.db.models.signals import post_save
from django.dispatch import receiver

from certificate.models import OrderCertificate


@shared_task()
@receiver(post_save, sender=OrderCertificate)
def send_feedback_email_task(sender, instance: OrderCertificate, created, **kwargs):
    # print(OrderCreateView)
    if created:
        send_mail('Contact Form',
                  f'{instance.info}'
                  f'Сертификат на Тур:{instance.tours},'
                  f'стоимость {instance.tours.price} сом',
                  settings.EMAIL_HOST_USER,
                  [f'{instance.email}'],
                  fail_silently=False)
