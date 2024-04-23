from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = PhoneNumberField(max_length=20, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар', help_text='Загрузите аватар', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name="Страна", **NULLABLE)
    token = models.CharField(max_length=100, verbose_name="Код верификации", **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
