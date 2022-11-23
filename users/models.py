from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4

from phone_field import PhoneField


class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, phone, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        if not username:
            raise ValueError("Вы не ввели Логин")
        if not phone:
            raise ValueError("Вы не ввели Телефон")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password, phone):
        return self._create_user(email, username, password, phone)

    def create_superuser(self, email, username, password, phone):
        return self._create_user(email, username, password, phone, is_staff=True, is_superuser=True)


class CustomUser(AbstractUser):
    phone = PhoneField(unique=True, blank=False, null=False)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)  # Статус активации
    is_staff = models.BooleanField(default=True)  # Статус админа
    email_verify = models.UUIDField(default=uuid4())

    USERNAME_FIELD = 'email'  # Идентификатор для обращения
    REQUIRED_FIELDS = ['username', 'phone']  # Список имён полей для Superuser

    objects = MyUserManager()

    def __str__(self):
        return f'{self.email_verify}'


# Профиль пользователя
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE,
                                related_name='user')
    age = models.IntegerField(null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.user}'


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        host = 'http://127.0.0.1:8000/auth/emailVerification/'
        use1 = instance.email
        use2 = instance.email_verify
        send_mail('Contact Form',
                  f'{host}'
                  f'{use1}, {use2}',
                  settings.EMAIL_HOST_USER,
                  [f'{instance.email}'],
                  fail_silently=False)

        UserProfile.objects.create(user=instance)
