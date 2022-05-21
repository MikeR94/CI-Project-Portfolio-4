from django import forms
from Reviews.models import Review
import re

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'body']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'pattern':'[A-Za-z ]+', 'title':'Please enter characters only'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'pattern':'[A-Za-z ]+', 'title':'Please enter characters only'}),
        }

    def clean_body(self):
        body = self.cleaned_data['body']
        if re.match('/[\s]+$',body):
            raise forms.ValidationError("Spaces not allowed")
        return body