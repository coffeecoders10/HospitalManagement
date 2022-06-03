# Generated by Django 2.2.6 on 2020-05-27 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DHOPD', '0021_auto_20200527_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_h',
            fields=[
                ('patient_id', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('patient_fname', models.CharField(max_length=200)),
                ('patient_mname', models.CharField(max_length=200)),
                ('patient_lname', models.CharField(max_length=200)),
                ('patient_gender', models.CharField(max_length=20)),
                ('patient_age', models.CharField(max_length=20)),
                ('patient_title', models.CharField(max_length=20)),
                ('patient_address', models.CharField(max_length=500)),
                ('patient_town', models.CharField(max_length=200)),
                ('patient_phone', models.CharField(max_length=15)),
                ('patient_imp', models.CharField(max_length=15)),
                ('patient_services', models.CharField(max_length=500)),
                ('patient_status', models.CharField(max_length=2)),
                ('patient_room', models.CharField(max_length=15)),
                ('patient_cost', models.CharField(max_length=100)),
                ('patient_date', models.DateField(default=datetime.date.today)),
                ('patient_time', models.TimeField(auto_now_add=True)),
                ('patient_comment', models.CharField(max_length=200)),
            ],
        ),
    ]
