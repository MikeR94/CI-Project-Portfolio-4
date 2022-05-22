from django import forms
from Booking.models import Booking
from Staff.models import Payment

# class TimeInput(forms.TimeInput):
#     input_type = 'time'

# class DateInput(forms.DateInput):
#     input_type = 'date'


# class EditBookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['first_name', 'last_name', 'contact_number', "time_of_visit", "date_of_visit", "number_of_guests", "email"]
#         widgets = {
#             'date_of_visit': DateInput(),
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 'pattern':'[A-Za-z ]+', 'title':'Please enter characters only'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control', 'pattern':'[A-Za-z ]+', 'title':'Please enter characters only'}),
#             'time_of_visit': forms.Select(attrs={'class': 'form-control'}),
#         }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount_owed', 'amount_paid', 'amount_tipped', 'total_income']
        widgets = {
            'total_income': forms.HiddenInput(),
            'amount_tipped': forms.HiddenInput(),
            }
