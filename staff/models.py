from django.db import models
from booking.models import Booking
from django.core.validators import BaseValidator
from decimal import Decimal

# Create your models here.


class MinValueValidator(BaseValidator):
    message = "Ensure this value is greater than 0."
    code = "min_value"

    def compare(self, a, b):
        return a < b


class Payment(models.Model):
    amount_owed = models.DecimalField(
        max_digits=60,
        decimal_places=2,
        blank=False,
        validators=[MinValueValidator(Decimal("0.01"))],
    
    )
    amount_paid = models.DecimalField(
        max_digits=60,
        decimal_places=2,
        blank=False,
        validators=[MinValueValidator(Decimal("0.01"))],
    
    )
    amount_tipped = models.DecimalField(
        max_digits=60, decimal_places=2, blank=True,)
    total_income = models.DecimalField(
        max_digits=60, decimal_places=2, null=False, blank=True,
    )
    booking = models.ForeignKey(Booking, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.total_income
