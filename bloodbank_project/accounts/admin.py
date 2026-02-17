from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    
    # ---------- LIST VIEW (the table of all users) ----------
    list_display = (
        'phone_number',   # column 1
        'email',          # column 2
        'get_full_name',  # column 3 (calls the method on your model)
        'blood_type',     # column 4
        'is_donor',       # column 5
        'is_receiver',    # column 6
        'is_hospital',    # column 7
        'is_active',      # column 8
        'date_joined',    # column 9
    )
    
    list_filter = (
        'blood_type',     # filter sidebar: by blood type
        'is_donor',       # filter sidebar: by donor status
        'is_receiver',    # filter sidebar: by receiver status
        'is_hospital',    # filter sidebar: by hospital status
        'is_active',      # filter sidebar: by active status
    )
    
    search_fields = (
        'phone_number',   # search bar searches phone
        'email',          # search bar searches email
        'first_name',     # search bar searches first name
        'last_name',      # search bar searches last name
    )
    
    ordering = ('-date_joined',)  # newest users first
    
    # ---------- DETAIL VIEW (clicking one user to edit) ----------
    fieldsets = (
        # Section 1: Login credentials
        ('Login Credentials', {
            'fields': ('phone_number', 'email', 'password')
        }),
        # Section 2: Personal information
        ('Personal Information', {
            'fields': (
                'first_name',
                'last_name',
                'age',
                'address',
                'blood_type',
            )
        }),
        # Section 3: Roles in the blood bank system
        ('Roles', {
            'fields': ('is_donor', 'is_receiver', 'is_hospital')
        }),
        # Section 4: Django system permissions
        ('System Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        # Section 5: Important dates
        ('Important Dates', {
            'fields': ('date_joined', 'last_login')
        }),
    )
    
    # ---------- ADD VIEW (the form when creating a NEW user from admin) ----------
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # makes the form wider in admin
            'fields': (
                'phone_number',
                'email',
                'first_name',
                'last_name',
                'age',
                'address',
                'blood_type',
                'is_donor',
                'is_receiver',
                'is_hospital',
                'password1',   # password (enter)
                'password2',   # password (confirm)
            ),
        }),
    )
    
    # These fields are read-only (can see but not edit)
    readonly_fields = ('date_joined', 'last_login')