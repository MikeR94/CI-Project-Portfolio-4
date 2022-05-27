from django import forms
from Booking.models import Booking
from datetime import date
import calendar
from django.utils import timezone

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ["first_name", "last_name", "email", "time_of_visit", "date_of_visit", "number_of_guests", "contact_number", "additional_info", "disabled_access"]
        widgets = {
            'date_of_visit': DateInput(),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'pattern':'[A-Za-z ]+', 'title':'Please enter characters only'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'pattern':'[A-Za-z ]+', 'title':'Please enter characters only'}),
            'time_of_visit': forms.Select(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'type':'number'})
        }

    def clean(self):
        cleaned_data = super(BookingForm, self).clean()
        time_of_visit = cleaned_data.get('time_of_visit')
        date_of_visit = cleaned_data.get('date_of_visit')
        today = date.today()
        time = timezone.now().time()

        year = 2022
        A=calendar.TextCalendar(calendar.SUNDAY)
        for b in range(1,13):
            for k in A.itermonthdays(year,b):
                if k!=0:
                    day=date(year, b,k)
                    if day.weekday()==6:
                        sunday1 = (f'{year}-0{b}-{k}')
                        sunday2 = (f'{year}-{b}-{k}')
                        if str(date_of_visit) == str(sunday1):
                            self._errors['date_of_visit'] = self.error_class(['Sorry we are closed on sundays'])
                            del self.cleaned_data['date_of_visit']
                        if str(date_of_visit) == str(sunday2):
                            self._errors['date_of_visit'] = self.error_class(['Sorry we are closed on sundays'])
                            del self.cleaned_data['date_of_visit']

        if date_of_visit == today and time_of_visit < time:
            self._errors['time_of_visit'] = self.error_class(['You cant book in the past'])
            del self.cleaned_data['time_of_visit']
        return cleaned_data
        
    
