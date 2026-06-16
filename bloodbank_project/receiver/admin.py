from django.contrib import admin
from .models import BloodRequest


@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = (
        'receiver',
        'blood_type',
        'units',
        'urgency',
        'hospital',
        'status',
        'requested_on',
    )
    list_filter = ('blood_type', 'urgency', 'status')
    search_fields = (
        'receiver__phone_number',
        'receiver__first_name',
        'receiver__last_name',
        'hospital',
    )
    list_editable = ('status',)  
    ordering = ('-requested_on',)