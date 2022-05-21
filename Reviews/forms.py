from django import forms
from Reviews.models import Review
import re

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'body']
        first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
        last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))

    def clean_body(self):
        body = self.cleaned_data['body']
        if re.match('/[\s]+$',body):
            raise forms.ValidationError("Spaces not allowed")
        return body