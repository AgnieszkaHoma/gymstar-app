# Generated by Django 4.1.2 on 2022-10-15 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
    ]
