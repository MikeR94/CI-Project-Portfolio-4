from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["first_name", "last_name", "stars", "body"]
        widgets = {
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
            "stars": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }
