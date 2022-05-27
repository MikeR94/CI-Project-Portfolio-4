# Generated by Django 4.0.3 on 2022-05-27 10:27

import Staff.models
from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_owed', models.DecimalField(decimal_places=2, max_digits=6, validators=[Staff.models.MinValueValidator(Decimal('0.01'))])),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=6, validators=[Staff.models.MinValueValidator(Decimal('0.01'))])),
                ('amount_tipped', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('total_income', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Booking.booking')),
            ],
        ),
    ]
