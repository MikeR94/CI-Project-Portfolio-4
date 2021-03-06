# Generated by Django 4.0.4 on 2022-06-08 08:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import reviews.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=25, validators=[reviews.utils.validate_not_spaces]
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=25, validators=[reviews.utils.validate_not_spaces]
                    ),
                ),
                (
                    "body",
                    models.TextField(
                        validators=[
                            reviews.utils.validate_not_spaces,
                            django.core.validators.MinLengthValidator(
                                80, "The field must contain at least 80 characters"
                            ),
                        ]
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("approved", models.BooleanField(default=False)),
                ("acknowledged", models.BooleanField(default=False)),
                (
                    "stars",
                    models.CharField(
                        choices=[
                            ("1 Star", "1 star"),
                            ("2 Star", "2 star"),
                            ("3 Star", "3 star"),
                            ("4 Star", "4 star"),
                            ("5 Star", "5 star"),
                        ],
                        default="5 Star",
                        max_length=6,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
