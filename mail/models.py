from django.db import models

from users.models import User


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='почта')
    full_name = models.CharField(max_length=35, verbose_name='Ф.И.О.', **NULLABLE)
    comment = models.CharField(max_length=250, verbose_name='комментарий', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        permissions = [
            ("disable_client", "Can disable client"),
        ]


class EmailSettings(models.Model):
    PERIODS = {
        'PD': 'Раз в день',
        'PW': 'Раз в неделю',
        'PM': 'Раз в месяц',
        'PY': 'Раз в год',
    }
    STATUSES = {
        'CREATED': 'Создана',
        'RUN': 'Запущена',
        'CLOSE': 'Завершена',
    }
    first_datetime = models.DateTimeField(auto_now_add=True, verbose_name='дата и время первой отправки рассылки')
    periodicity = models.CharField(max_length=2, choices=PERIODS, default='PW', verbose_name='периодичность')
    status = models.CharField(max_length=10, choices=STATUSES, default='CREATED', verbose_name='статус')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.periodicity} - {self.status}'

    def stop_mailing(self):
        self.status = 'CLOSE'
        self.save()

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылки'
        permissions = [
            ("disable_mailing", "Can disable mailing"),
        ]


class EmailMessage(models.Model):
    head = models.CharField(max_length=150, verbose_name='заголовок письма')
    body = models.TextField(verbose_name='тело письма')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.head}'

    class Meta:
        verbose_name = 'сообщение рассылки'
        verbose_name_plural = 'сообщения рассылок'


class EmailTry(models.Model):
    last_try_datetime = models.DateTimeField(auto_now=True, verbose_name='дата и время последней попытки')
    try_status = models.BooleanField(default=False, verbose_name='статус попытки')
    server_answer = models.CharField(max_length=250, verbose_name='ответ почтового сервера', **NULLABLE)

    def __str__(self):
        return f'{self.try_status} ({self.last_try_datetime})'

    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылок'
