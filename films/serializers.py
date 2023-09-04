from django import forms
from .validators import validate_possible_number
from .models import Transaction
from django.core.exceptions import ValidationError


class MpesaCheckoutForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = (
            "phone_number",
            "amount",
            "reference",
            "description",
        )

    def clean_phone_number(self):
        """A very basic validation to remove the preceding + or replace the 0 with 254"""
        phone_number = self.cleaned_data['phone_number']
        if phone_number[0] == "+":
            phone_number = phone_number[1:]
        if phone_number[0] == "0":
            phone_number = "254" + phone_number[1:]
        try:
            validate_possible_number(phone_number, "KE")
        except ValidationError:
            raise forms.ValidationError("Phone number is not valid")
        return phone_number

    def clean_amount(self):
        """This method validates the amount"""
        amount = self.cleaned_data['amount']
        if not amount or float(amount) <= 0:
            raise forms.ValidationError("Amount must be greater than Zero")
        return amount

    def clean_reference(self):
        """Write your validation logic here"""
        reference = self.cleaned_data['reference']
        if reference:
            return reference
        return "Test"

    def clean_description(self):
        """Write your validation logic here"""
        description = self.cleaned_data['description']
        if description:
            return description
        return "Test"
