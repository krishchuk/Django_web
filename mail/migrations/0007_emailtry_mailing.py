# Generated by Django 5.0.4 on 2024-05-06 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0006_remove_emailsettings_first_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtry',
            name='mailing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mail.emailsettings', verbose_name='рассылка'),
        ),
    ]
