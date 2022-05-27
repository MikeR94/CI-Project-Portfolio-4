import random
from django.utils import timezone
from django import forms

def create_new_ref_number():
      return str(random.randint(1000000000, 9999999999))

def validate_date(date):
    if date < timezone.now().date():
        raise forms.ValidationError("Date cannot be in the past")


