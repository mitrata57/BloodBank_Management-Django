from django import forms
from .models import BloodRequest


class BloodRequestForm(forms.Form):

    blood_type = forms.ChoiceField(
        choices=BloodRequest.BLOOD_TYPE_CHOICES,
        error_messages={'required': 'Please select blood type needed'}
    )
    units = forms.DecimalField(
        max_digits=4,
        decimal_places=1,
        initial=1.0,
        min_value=0.5,
        max_value=10.0,
        error_messages={
            'required': 'Please enter units needed',
            'min_value': 'Minimum is 0.5 units',
            'max_value': 'Maximum is 10.0 units'
        }
    )
    urgency = forms.ChoiceField(
        choices=BloodRequest.URGENCY_CHOICES,
        error_messages={'required': 'Please select urgency level'}
    )
    hospital = forms.CharField(
        max_length=255,
        error_messages={'required': 'Please enter hospital name'}
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        error_messages={'required': 'Please enter reason for blood requirement'}
    )
    notes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2}),
        required=False
    )