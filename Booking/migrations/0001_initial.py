# Generated by Django 4.0.3 on 2022-05-27 10:27

import Booking.models
import Booking.utils
import datetime
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('ref_number', models.CharField(blank=True, default=Booking.utils.create_new_ref_number, editable=False, max_length=10, unique=True)),
                ('date_of_visit', models.DateField(validators=[Booking.utils.validate_date])),
                ('time_of_visit', models.TimeField(choices=[(datetime.time(7, 0), '07:00'), (datetime.time(10, 0), '10:00'), (datetime.time(10, 30), '10:30'), (datetime.time(17, 0), '17:00'), (datetime.time(17, 30), '17:30'), (datetime.time(18, 0), '18:00'), (datetime.time(18, 30), '18:30'), (datetime.time(19, 0), '19:00'), (datetime.time(19, 30), '19:30'), (datetime.time(20, 0), '20:00'), (datetime.time(20, 30), '20:30'), (datetime.time(21, 0), '21:00'), (datetime.time(21, 30), '21:30'), (datetime.time(22, 0), '22:00'), (datetime.time(22, 30), '22:30')])),
                ('number_of_guests', models.PositiveIntegerField(validators=[Booking.models.MinValueValidator(Decimal('0.01'))])),
                ('guest_attended', models.BooleanField(default=False)),
                ('guest_no_show', models.BooleanField(default=False)),
                ('no_show_email_sent', models.BooleanField(default=False)),
                ('contact_number', models.CharField(default='', max_length=15)),
                ('bill_settled', models.BooleanField(default=False)),
                ('bill_submitted', models.BooleanField(default=False)),
                ('booking_approved', models.BooleanField(default=False)),
                ('booking_denied', models.BooleanField(default=False)),
                ('booking_acknowledged', models.BooleanField(default=False)),
                ('disabled_access', models.BooleanField(default=False)),
                ('additional_info', models.TextField(blank=True, default='', max_length=150)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
