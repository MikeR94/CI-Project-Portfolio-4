from django import forms


def validate_not_spaces(value):
    if isinstance(value, str) and value.strip() == "":
        raise forms.ValidationError(
            "You must provide more than just whitespace."
        )
