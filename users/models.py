from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE,
                             help_text='Введите номер телефона')
    token = models.CharField(max_length=100, verbose_name='токен', **NULLABLE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        """Может блокировать пользователей сервисa"""
        permissions = [
            ('can_edit_is_active', 'can edit is_active')
        ]

    def __str__(self):
        return self.email
