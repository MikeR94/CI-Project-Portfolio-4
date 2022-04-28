from django import forms
from Booking.models import Booking

class EditBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'contact_number', "time_of_visit", "date_of_visit", "number_of_guests", "guest_attended", "bill_settled", "booking_approved", "booking_denied", "booking_acknowledged", "email"]