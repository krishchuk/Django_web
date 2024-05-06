# Generated by Django 5.0.4 on 2024-05-06 16:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0007_emailtry_mailing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsettings',
            name='date_end',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата окончания рассылки'),
        ),
        migrations.AlterField(
            model_name='emailsettings',
            name='date_start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата начала рассылки'),
        ),
    ]
