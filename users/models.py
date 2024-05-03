from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    full_name = models.CharField(max_length=35, verbose_name='Ф.И.О.')
    comment = models.CharField(max_length=250, verbose_name='комментарий', null=True, blank=True)
    verification_code = models.CharField(max_length=9, verbose_name='Код верификации', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username} {self.email}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
