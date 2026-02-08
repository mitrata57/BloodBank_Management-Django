from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.

phone_regex = RegexValidator(
    regex = r'^(\+977)?[9][6-9]\d{8}$',
    message = "Phone number must be in format: '9841234580' or '+9779841234580'"
    
)
class CustomUserManager(BaseUserManager):
    """Manager for CustomUser model."""
    
    def create_user(self, phone_number, email, password=None, **extra_fields):
        """regular user."""
        if not phone_number:
            raise ValueError('Phone number is required')
        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        phone_number = phone_number.replace(' ', '').replace('-', '')
        
        user = self.model(
            phone_number=phone_number,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone_number, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(phone_number, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    BLOOD_TYPE_CHOICES = [
        ('A+', 'A Positive'),
        ('A-', 'A Negative'),
        ('B+', 'B Positive'),
        ('B-', 'B Negative'),
        ('O+', 'O Positive'),
        ('O-', 'O Negative'),
        ('AB+', 'AB Positive'),
        ('AB-', 'AB Negative'),
    ]
    
    # Authentication fields
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[phone_regex],
        help_text='Format: 9841234567 or +9779841234567'
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        help_text='Required for login and notifications'
    )
    
    # Personal info
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    
    # Blood info
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    
    # Role flags
    is_donor = models.BooleanField(default=False, help_text='Can donate blood')
    is_receiver = models.BooleanField(default=False, help_text='Can request blood')
    is_hospital = models.BooleanField(default=False, help_text='Hospital account')
    
    # Django required
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'blood_type', 'age', 'address']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.phone_number})"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        return self.first_name
    
    @property
    def roles(self):
        roles = []
        if self.is_donor:
            roles.append('Donor')
        if self.is_receiver:
            roles.append('Receiver')
        if self.is_hospital:
            roles.append('Hospital')
        return roles
