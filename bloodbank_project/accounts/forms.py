from django import forms
from django.core.validators import RegexValidator
from .models import CustomUser


#  reusing it here for form validation
phone_regex = RegexValidator(
    regex=r'^(\+977)?[9][6-9]\d{8}$',
    message="Phone number must be in format: '9841123456' or '+9779841123456'"
)


class CustomUserCreationForm(forms.Form):
    
    # --- Role field ---
    ROLE_CHOICES = [
        ('donor', 'Donor'),
        ('receiver', 'Receiver'),
        ('hospital', 'Hospital'),
    ]
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect,
        error_messages={'required': 'Please select a role'}
    )

    # --- Personal info fields ---
    first_name = forms.CharField(
        max_length=50,
        error_messages={'required': 'First name is required'}
    )
    last_name = forms.CharField(
        max_length=50,
        error_messages={'required': 'Last name is required'}
    )
    email = forms.EmailField(
        error_messages={
            'required': 'Email is required',
            'invalid': 'Enter a valid email address'
        }
    )
    phone_number = forms.CharField(
        validators=[phone_regex],  # Nepal format validation happens here
        error_messages={'required': 'Phone number is required'}
    )
    blood_type = forms.ChoiceField(
        choices=CustomUser.BLOOD_TYPE_CHOICES,
        error_messages={'required': 'Blood type is required'}
    )
    age = forms.IntegerField(
        min_value=1,
        max_value=65,
        error_messages={
            'required': 'Age is required',
            'min_value': 'Enter valid age',
            'max_value': 'Age cannot exceed 65'
        }
    )
    address = forms.CharField(
        max_length=255,
        error_messages={'required': 'Address is required'}
    )

    # --- Password fields ---
    password = forms.CharField(
        widget=forms.PasswordInput,  # renders as <input type="password">
        min_length=8,
        error_messages={
            'required': 'Password is required',
            'min_length': 'Password must be at least 8 characters'
        }
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Please confirm your password'}
    )

    # --- Custom validation methods ---

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered')
        return email 

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        phone = phone.replace(' ', '').replace('-', '')
        if CustomUser.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError('This phone number is already registered')
        return phone

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('Passwords do not match')

        return cleaned_data
    


class ProfileEditForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        error_messages={'required': 'First name is required'}
    )
    last_name = forms.CharField(
        max_length=50,
        error_messages={'required': 'Last name is required'}
    )
    email = forms.EmailField(
        error_messages={
            'required': 'Email is required',
            'invalid': 'Enter a valid email address'
        }
    )
    blood_type = forms.ChoiceField(
        choices=CustomUser.BLOOD_TYPE_CHOICES,
        error_messages={'required': 'Blood type is required'}
    )
    age = forms.IntegerField(
        min_value=1,
        max_value=120,
        error_messages={
            'required': 'Age is required',
            'min_value': 'Please enter a valid age',
            'max_value': 'Please enter a valid age'
        }
    )
    address = forms.CharField(
        max_length=255,
        error_messages={'required': 'Address is required'}
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exclude(id=self.user.id).exists():
            raise forms.ValidationError('This email is already in use by another account')
        return email
    
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Please enter your current password'}
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        error_messages={
            'required': 'Please enter a new password',
            'min_length': 'Password must be at least 8 characters'
        }
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Please confirm your new password'}
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Current password is incorrect')
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError('New passwords do not match')

        return cleaned_data