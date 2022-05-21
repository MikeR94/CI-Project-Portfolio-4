from django import forms
from Booking.models import Booking
from Staff.models import Payment


class DateInput(forms.DateInput):
    input_type = 'date'

class EditBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'contact_number', "time_of_visit", "date_of_visit", "number_of_guests", "email"]
        widgets = {
            'date_of_visit': DateInput(),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount_owed', 'amount_paid', 'amount_tipped', 'total_income']
        widgets = {
            'total_income': forms.HiddenInput(),
            'amount_tipped': forms.HiddenInput(),
            }
