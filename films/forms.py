from django import forms

class MpesaCheckoutForm(forms.Form):
    email = forms.EmailField(required=True, label='Email')
    phone_number = forms.CharField(max_length=20, required=True, label='Phone Number')
    amount = forms.DecimalField(required=True, max_digits=10, decimal_places=2, label='Amount')
