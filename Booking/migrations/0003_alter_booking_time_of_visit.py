# Generated by Django 4.0.4 on 2022-05-24 10:41

import Booking.utils
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0002_alter_booking_time_of_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time_of_visit',
            field=models.TimeField(choices=[(datetime.time(10, 0), '10:00'), (datetime.time(10, 30), '10:30'), (datetime.time(17, 0), '17:00'), (datetime.time(17, 30), '17:30'), (datetime.time(18, 0), '18:00'), (datetime.time(18, 30), '18:30'), (datetime.time(19, 0), '19:00'), (datetime.time(19, 30), '19:30'), (datetime.time(20, 0), '20:00'), (datetime.time(20, 30), '20:30'), (datetime.time(21, 0), '21:00'), (datetime.time(21, 30), '21:30'), (datetime.time(22, 0), '22:00'), (datetime.time(22, 30), '22:30')], validators=[Booking.utils.validate_time]),
        ),
    ]
