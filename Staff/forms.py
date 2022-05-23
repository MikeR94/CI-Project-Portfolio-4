from django import forms
from Staff.models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount_owed', 'amount_paid', 'amount_tipped', 'total_income']
        widgets = {
            'total_income': forms.HiddenInput(),
            'amount_tipped': forms.HiddenInput(),
            }
