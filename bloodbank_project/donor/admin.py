from django.contrib import admin
from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = (
        'donor',
        'blood_type',
        'units',
        'donated_on',
        'location',
        'is_verified',
    )
    list_filter = ('blood_type', 'is_verified', 'donated_on')
    search_fields = ('donor__phone_number', 'donor__first_name', 'donor__last_name')
    list_editable = ('is_verified',)  
    ordering = ('-donated_on',)