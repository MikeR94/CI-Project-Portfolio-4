from django import forms
from Booking.models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ["first_name", "last_name", "email", "time_of_visit", "date_of_visit", "number_of_guests", "contact_number", "disabled_access"]
        widgets = {
            'date_of_visit': DateInput(),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'pattern':'[A-Za-z ]+', 'title':'Please enter characters only'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'pattern':'[A-Za-z ]+', 'title':'Please enter characters only'}),
            'time_of_visit': forms.Select(attrs={'class': 'form-control'}),
        }
    
