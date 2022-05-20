from django.db import models
from datetime import datetime
from Accounts.models import User
from Booking.utils import create_new_ref_number, validate_date

# Create your models here.

class Booking(models.Model):
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    ref_number = models.CharField(max_length=10, blank=True, editable=False, unique=True, default=create_new_ref_number)
    date_of_visit = models.DateField(auto_now=False, auto_now_add=False, validators=[validate_date])
    time_of_visit = models.TimeField(choices=(
        (datetime.strptime('5:00 pm', "%I:%M %p").time(), '17:00'),
        (datetime.strptime('5:30 pm', "%I:%M %p").time(), '17:30'),
        (datetime.strptime('6:00 pm', "%I:%M %p").time(), '18:00'),
        (datetime.strptime('6:30 pm', "%I:%M %p").time(), '18:30'),
        (datetime.strptime('7:00 pm', "%I:%M %p").time(), '19:00'),
        (datetime.strptime('7:30 pm', "%I:%M %p").time(), '19:30'),
        (datetime.strptime('8:00 pm', "%I:%M %p").time(), '20:00'),
        (datetime.strptime('8:30 pm', "%I:%M %p").time(), '20:30'),
        (datetime.strptime('9:00 pm', "%I:%M %p").time(), '21:00'),
        (datetime.strptime('9:30 pm', "%I:%M %p").time(), '21:30'),
        (datetime.strptime('10:00 pm', "%I:%M %p").time(), '22:00'),
        (datetime.strptime('10:30 pm', "%I:%M %p").time(), '22:30'),

    ))
    number_of_guests = models.PositiveIntegerField(blank=False, null=False)
    guest_attended = models.BooleanField(default=False)
    guest_no_show = models.BooleanField(default=False)
    contact_number = models.IntegerField(default="")
    bill_settled = models.BooleanField(default=False)
    booking_approved = models.BooleanField(default=False)
    booking_denied = models.BooleanField(default=False)
    booking_acknowledged = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name