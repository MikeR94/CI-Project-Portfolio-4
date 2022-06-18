from django.apps import AppConfig


class StaffConfig(AppConfig):
    """
    A class that holds config info
    for the staff app
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "staff"
