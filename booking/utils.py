import random
from django.utils import timezone
from django import forms


def create_new_ref_number():
    """
    Generates a new random number
    used for booking references
    """
    return str(random.randint(1000000000, 9999999999))


def validate_date(date):
    """
    A function that validates if
    the users chosen date is not
    in the past
    """
    if date < timezone.now().date():
        raise forms.ValidationError("You can't book in the past")


# All the dates for every sunday in 2022
sunday = [
    "2022-01-02",
    "2022-01-09",
    "2022-01-16",
    "2022-01-23",
    "2022-01-30",
    "2022-02-06",
    "2022-02-13",
    "2022-02-20",
    "2022-02-27",
    "2022-03-06",
    "2022-03-13",
    "2022-03-20",
    "2022-03-27",
    "2022-04-03",
    "2022-04-10",
    "2022-04-17",
    "2022-04-24",
    "2022-05-01",
    "2022-05-08",
    "2022-05-15",
    "2022-05-22",
    "2022-05-29",
    "2022-06-05",
    "2022-06-12",
    "2022-06-19",
    "2022-06-26",
    "2022-07-03",
    "2022-07-10",
    "2022-07-17",
    "2022-07-24",
    "2022-07-31",
    "2022-08-07",
    "2022-08-14",
    "2022-08-21",
    "2022-08-28",
    "2022-09-04",
    "2022-09-11",
    "2022-09-18",
    "2022-09-25",
    "2022-10-02",
    "2022-10-09",
    "2022-10-16",
    "2022-10-23",
    "2022-10-30",
    "2022-11-06",
    "2022-11-13",
    "2022-11-20",
    "2022-11-27",
    "2022-12-04",
    "2022-12-11",
    "2022-12-18",
    "2022-12-25",
]
