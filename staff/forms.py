from django import forms
from staff.models import Payment


class PaymentForm(forms.ModelForm):
    """
    A class to create a Payment form
    from the Payment model
    """
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
        """
        A function to clean the form data
        and perform custom form validation
        """
        cleaned_data = super(PaymentForm, self).clean()
        amount_paid = cleaned_data.get("amount_paid")
        amount_owed = cleaned_data.get("amount_owed")

        if amount_paid > 99999:
            self._errors["amount_paid"] = self.error_class(
                [
                    """Please enter a number lower
                    than 6 digits"""
                ]
            )
        if amount_owed > 99999:
            self._errors["amount_owed"] = self.error_class(
                [
                    """Please enter a number lower
                    than 6 digits"""
                ]
            )

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
