from django import forms
from Booking.models import Booking
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ["first_name", "last_name", "email", "time_of_visit", "date_of_visit", "number_of_guests", "contact_number"]
        widgets = {
            'date_of_visit': DateInput(),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'time_of_visit': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_first_name(self):

        first_name = self.cleaned_data.get('first_name')

        
        for instance in Booking.objects.all():
            if instance.first_name == first_name:
                raise forms.ValidationError("There is a booking under this name already")
        
        return first_name
