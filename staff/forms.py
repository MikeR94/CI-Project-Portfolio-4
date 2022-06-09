from django import forms
from staff.models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            "amount_owed",
            "amount_paid",
            "amount_tipped",
            "total_income",
        ]
        widgets = {
            "total_income": forms.HiddenInput(),
            "amount_tipped": forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super(PaymentForm, self).clean()
        amount_paid = cleaned_data.get("amount_paid")
        amount_owed = cleaned_data.get("amount_owed")

        if amount_paid < amount_owed:
            self._errors["amount_paid"] = self.error_class(
                [
                    """This bill has not been settled.
                    Please settle this bill before submitting payment
                    information"""
                ]
            )
            self._errors["amount_owed"] = self.error_class(
                [
                    """This bill has not been settled.
                    Please settle this bill before submitting payment
                    information"""
                ]
            )
            del self.cleaned_data["amount_paid"]
            del self.cleaned_data["amount_owed"]
        return cleaned_data
