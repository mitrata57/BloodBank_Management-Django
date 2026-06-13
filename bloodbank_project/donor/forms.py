from django import forms
from .models import Donation


class DonationForm(forms.Form):
    
    donated_on = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        error_messages={'required': 'Please enter the donation date'}
    )
    location = forms.CharField(
        max_length=255,
        error_messages={'required': 'Please enter the donation location'}
    )
    units = forms.DecimalField(
        max_digits=4,
        decimal_places=1,
        initial=1.0,
        min_value=0.5,
        max_value=5.0,
        error_messages={
            'required': 'Please enter units donated',
            'min_value': 'Minimum donation is 0.5 units',
            'max_value': 'Maximum donation is 5.0 units'
        }
    )
    notes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )

    def clean_donated_on(self):
        from django.utils import timezone
        donated_on = self.cleaned_data.get('donated_on')
        today = timezone.now().date()
        
        if donated_on > today:
            raise forms.ValidationError('Donation date cannot be in the future')
        
        return donated_on