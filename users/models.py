from django.utils.log import request_logger
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
        if len(password) < 8:
            raise ValueError("Пароль должен содержать не менее 8 символов")
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

    def create_superuser(self, email, username, password, phone, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(' is_superuser=True.')

        return self._create_user(
            email=email,
            username=username,
            password=password,
            phone=phone,
            **extra_fields
        )


class CustomUser(AbstractUser):
    """ Модель пользователя """
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
    image = models.ImageField(blank=False, null=True, upload_to="profile_images")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE,
                                related_name='user')
    age = models.IntegerField(null=True)
    birth_date = models.DateField('Дата Рождения', blank=False, null=True, default='2000-01-12')
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = PhoneNumberField(null=True, region='KG', unique=True, )

    def __str__(self):
        return f'{self.user}'

    def profile_image_path(instance, filename):
        # Generate a dynamic relative path for storing the profile image
        return f"user_{instance.user.id}/profile_images/{filename}"


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    """Сигнал Для создания Пользователя и его Профиль"""
    if created:
        # Отправляем электронное письмо со ссылкой для подтверждения адреса электронной почты
        send_mail(
            "Подтверждение адреса электронной почты",
            f"http://127.0.0.1:8000/users/email/verification/{instance.email_verify}",
            settings.EMAIL_HOST_USER,
            [f"{instance.email}"],
            fail_silently=False
        )

        # Создаем профиль пользователя
        UserProfile.objects.create(user=instance)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = reset_password_token.key

    # Формируем сообщение электронной почты
    email_html_message = f'''
    Здравствуйте, {reset_password_token.user.username.capitalize()}!\n
    Мы получили запрос на восстановление пароля для вашего аккаунта.    
    Если вы не делали этого запроса, пожалуйста, проигнорируйте это сообщение.\n
    Чтобы сбросить ваш пароль, перейдите по ссылке ниже и введите ваш токен и новый пароль:
    "http://127.0.0.1:8000/users/password_reset/confirm/{email_plaintext_message}"
    
    Если у вас возникли какие-либо проблемы, 
    пожалуйста, свяжитесь с нами по электронной почте ниже 
    atashbaevnurjigit@gmail.com.
    С уважением, Команда поддержки'''

    try:
        # Отправляем электронное письмо с токеном для сброса пароля пользователю
        send_mail(
            "Восстановление пароля",
            email_html_message,
            "atashbaevnurjigit@gmail.com",
            (reset_password_token.user.email,)
        )
    except Exception as e:
        # Выдаём ошибку
        print(e)
