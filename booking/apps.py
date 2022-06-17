from django.apps import AppConfig


class BookingConfig(AppConfig):
    """
    A class that holds config info
    for the booking app
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "booking"
