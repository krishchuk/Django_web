# Generated by Django 5.0.4 on 2024-05-03 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('full_name', models.CharField(max_length=35, verbose_name='Ф.И.О.')),
                ('comment', models.CharField(blank=True, max_length=250, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=150, verbose_name='заголовок письма')),
                ('body', models.TextField(verbose_name='тело письма')),
            ],
            options={
                'verbose_name': 'сообщение рассылки',
                'verbose_name_plural': 'сообщения рассылок',
            },
        ),
        migrations.CreateModel(
            name='EmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_datetime', models.DateTimeField(auto_now_add=True, verbose_name='дата и время первой отправки рассылки')),
                ('periodicity', models.CharField(choices=[('PD', 'Раз в день'), ('PW', 'Раз в неделю'), ('PM', 'Раз в месяц'), ('PY', 'Раз в год')], default='PW', max_length=2, verbose_name='периодичность')),
                ('status', models.CharField(choices=[('CREATED', 'Создана'), ('RUN', 'Запущена'), ('CLOSE', 'Завершена')], default='CREATED', max_length=10, verbose_name='статус')),
            ],
            options={
                'verbose_name': 'настройка рассылки',
                'verbose_name_plural': 'настройки рассылки',
            },
        ),
        migrations.CreateModel(
            name='EmailTry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_try_datetime', models.DateTimeField(auto_now=True, verbose_name='дата и время последней попытки')),
                ('try_status', models.BooleanField(default=False, verbose_name='статус попытки')),
                ('server_answer', models.CharField(blank=True, max_length=250, null=True, verbose_name='ответ почтового сервера')),
            ],
            options={
                'verbose_name': 'попытка рассылки',
                'verbose_name_plural': 'попытки рассылок',
            },
        ),
    ]
