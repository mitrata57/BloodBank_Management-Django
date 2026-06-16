from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


class BloodRequest(models.Model):

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

    URGENCY_CHOICES = [
        ('normal', 'Normal'),
        ('urgent', 'Urgent'),
        ('critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('fulfilled', 'Fulfilled'),
        ('rejected', 'Rejected'),
    ]

    receiver = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='blood_requests',
        limit_choices_to={'is_receiver': True}
    )

    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    units = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=1.0,
        help_text='Units of blood needed'
    )

    urgency = models.CharField(
        max_length=10,
        choices=URGENCY_CHOICES,
        default='normal'
    )

    hospital = models.CharField(
        max_length=255,
        help_text='Hospital where blood is needed'
    )
    reason = models.TextField(
        help_text='Reason for blood requirement'
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

 
    requested_on = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-requested_on']
        verbose_name = 'Blood Request'
        verbose_name_plural = 'Blood Requests'

    def __str__(self):
        return f"{self.receiver.get_full_name()} needs {self.blood_type} - {self.status}"

    @property
    def is_urgent(self):
        return self.urgency in ['urgent', 'critical']