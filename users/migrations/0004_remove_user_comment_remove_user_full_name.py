# Generated by Django 5.0.4 on 2024-05-04 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
    ]