# Generated by Django 2.2.6 on 2020-05-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DHOPD', '0008_auto_20200507_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_time',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='receipt_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
