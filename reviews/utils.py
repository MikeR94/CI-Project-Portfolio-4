from django import forms


def validate_not_spaces(value):
    """
    Function to detect if the user
    has input just spaces only
    """
    if isinstance(value, str) and value.strip() == "":
        raise forms.ValidationError(
            "You must provide more than just whitespace.")
