from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from uuid import uuid4
from phonenumber_field.modelfields import PhoneNumberField


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

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(' is_superuser=True.')

        return self._create_user(
            username=username,
            password=password,
            **extra_fields
        )


'''User Model'''


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    phone = PhoneNumberField(null=True, region='KG', unique=True, )
    birth_date = models.DateField('Дата Рождения', blank=False, null=True, default='2000-01-12')
    is_active = models.BooleanField(default=False)  # Статус активации
    is_staff = models.BooleanField(default=False)  # Статус админа
    email_verify = models.UUIDField(default=uuid4())

    USERNAME_FIELD = 'email'  # Идентификатор для обращения
    REQUIRED_FIELDS = ['username', 'phone']  # Список имён полей для Superuser

    objects = MyUserManager()

    def __str__(self):
        return f'{self.username, self.email_verify}'

    def email_verificate(self):
        self.is_active = True
        self.save(update_fields=['is_active'])


'''User Profile Model'''


class UserProfile(models.Model):
    image = models.ImageField(blank=False, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE,
                                related_name='user')
    age = models.IntegerField(null=True)
    birth_date = models.DateField('Дата Рождения', blank=False, null=True, default='2000-01-12')
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = PhoneNumberField(null=True, region='KG', unique=True, )

    def __str__(self):
        return f'{self.user}'


'''Creating user+profile signals'''


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        uuid = instance.email_verify
        send_mail('Contact Form',
                  f'http://127.0.0.1:8000/users/email/verification/{uuid}',
                  settings.EMAIL_HOST_USER,
                  [f'{instance.email}'],
                  fail_silently=False)

        UserProfile.objects.create(user=instance)


'''Password reset signal'''


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = reset_password_token.key

    send_mail(
        "Восстановление пароля",
        f'''
        Ваш токен для восстановления пароля
        Токен: {email_plaintext_message}. 
        Перейдите по ссылке, введите ваш токен и новый пароль
        http://127.0.0.1:8000/users/password_reset/confirm/''',
        "atashbaevnurjigit@gmail.com",
        [reset_password_token.user.email]
    )
