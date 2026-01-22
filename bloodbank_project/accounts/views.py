from django.shortcuts import render

# Remove the home() function - it belongs in core app!
# Remove the about() function - it belongs in core app!

def register(request):
    """Registration page - we'll build this properly tomorrow"""
    return render(request, 'accounts/register.html')

def login_view(request):
    """Login page - we'll build this tomorrow"""
    return render(request, 'accounts/login.html')