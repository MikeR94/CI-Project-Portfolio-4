from django import forms
from booking.models import Booking
from datetime import date, datetime
from booking.utils import sunday


class DateInput(forms.DateInput):
    """
    A class to register the input_type
    as date
    """
    input_type = "date"


class TimeInput(forms.TimeInput):
    """
    A class to register the input_type
    as time
    """
    input_type = "time"


class BookingForm(forms.ModelForm):
    """
    A class to create a Booking form
    from the Booking model
    """
    class Meta:
        model = Booking
        fields = [
            "first_name",
            "last_name",
            "email",
            "time_of_visit",
            "date_of_visit",
            "number_of_guests",
            "contact_number",
            "additional_info",
            "disabled_access",
        ]
        widgets = {
            "date_of_visit": DateInput(),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "pattern": "[A-Za-z ]+",
                    "title": "Please enter characters only",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "pattern": "[A-Za-z ]+",
                    "title": "Please enter characters only",
                }
            ),
            "time_of_visit": forms.Select(attrs={"class": "form-control"}),
            "contact_number": forms.TextInput(
                attrs={"class": "form-control", "type": "number"}
            ),
        }


    def clean(self):
        """
        A function to clean the form data
        and perform custom form validation
        """
        cleaned_data = super(BookingForm, self).clean()
        time_of_visit = cleaned_data.get("time_of_visit")
        date_of_visit = cleaned_data.get("date_of_visit")
        number_of_guests = cleaned_data.get("number_of_guests")
        today = date.today()
        time = datetime.now().time()

        if number_of_guests > 24:
                self._errors["number_of_guests"] = self.error_class(
                        ["Sorry we are only accept maximum bookings of 24"]
                    )
                del self.cleaned_data["number_of_guests"]

        for x in sunday:
            if x == str(date_of_visit):
                self._errors["date_of_visit"] = self.error_class(
                    ["Sorry we are closed on Sundays"]
                )
                del self.cleaned_data["date_of_visit"]

        if not "2022" in str(date_of_visit):
            self._errors["date_of_visit"] = self.error_class(
                ["Sorry we are only taking bookings for this year"]
            )
            del self.cleaned_data["date_of_visit"]

        if date_of_visit == today and time_of_visit < time:
            self._errors["time_of_visit"] = self.error_class(
                ["You can't book in the past"]
            )
            del self.cleaned_data["time_of_visit"]
        return cleaned_data
