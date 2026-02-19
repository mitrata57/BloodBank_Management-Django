from django.shortcuts import render
from accounts.decorators import hospital_required

def hospital_register(request):
    return render(request, 'hospital/register.html')

@hospital_required
def dashboard(request):
    return render(request, 'hospital/dashboard.html')