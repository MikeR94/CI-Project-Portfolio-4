# Generated by Django 3.2 on 2022-04-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='acknowledged',
            field=models.BooleanField(default=False),
        ),
    ]