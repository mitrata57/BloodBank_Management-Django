from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def donor_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Please login to access this page.')
            return redirect('accounts:login')
        
        if not request.user.is_donor:
            messages.error(request, 'You must be registered as a donor to access this page.')
            return redirect('core:home')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper


def receiver_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Please login to access this page.')
            return redirect('accounts:login')
        
        if not request.user.is_receiver:
            messages.error(request, 'You must be registered as a receiver to access this page.')
            return redirect('core:home')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper


def hospital_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Please login to access this page.')
            return redirect('accounts:login')
        
        if not request.user.is_hospital:
            messages.error(request, 'You must be registered as a hospital to access this page.')
            return redirect('core:home')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper