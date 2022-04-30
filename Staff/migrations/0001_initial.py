# Generated by Django 3.2 on 2022-04-29 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Booking', '0006_booking_guest_no_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_owed', models.DecimalField(decimal_places=2, max_digits=6)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=6)),
                ('amount_tipped', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('total_income', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Booking.booking')),
            ],
        ),
    ]