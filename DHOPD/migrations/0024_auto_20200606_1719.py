# Generated by Django 2.2.6 on 2020-06-06 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DHOPD', '0023_receipt_h'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt_h',
            name='receipt_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
