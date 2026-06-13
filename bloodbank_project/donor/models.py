from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


class Donation(models.Model):
    
    
    donor = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='donations',
        limit_choices_to={'is_donor': True}
    )
    
    
    donated_on = models.DateField(default=timezone.now)
    location = models.CharField(
        max_length=255,
        help_text='Hospital or blood bank where you donated'
    )
    
    
    blood_type = models.CharField(max_length=3)
    units = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=1.0,
        help_text='Units of blood donated (typically 1 unit = 450ml)'
    )
    
    is_verified = models.BooleanField(
        default=False,
        help_text='Verified by admin or hospital'
    )
    
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-donated_on']
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'
    
    def __str__(self):
        return f"{self.donor.get_full_name()} - {self.blood_type} on {self.donated_on}"