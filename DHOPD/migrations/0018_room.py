# Generated by Django 2.2.6 on 2020-05-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DHOPD', '0017_service_h'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('room_cost', models.CharField(max_length=200)),
                ('room_tag', models.CharField(max_length=200)),
            ],
        ),
    ]
