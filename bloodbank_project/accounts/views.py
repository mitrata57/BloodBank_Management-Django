from django.shortcuts import render



def register(request):
    
    return render(request, 'accounts/register.html')

def login_view(request):
    return render(request, 'accounts/login.html')