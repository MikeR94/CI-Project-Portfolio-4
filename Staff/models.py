from django.db import models
from Booking.models import Booking

# Create your models here.

class Payment(models.Model):
    amount_owed = models.DecimalField(max_digits=6, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    amount_tipped = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    total_income = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=True)
    booking = models.ForeignKey(Booking, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.total_income
