# Generated by Django 4.1.2 on 2023-01-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
