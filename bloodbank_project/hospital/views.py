from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def hospital_register(request):
    return render(request, 'hospital/register.html')

@login_required(login_url='accounts:login')
def dashboard(request):
    return render(request, 'hospital/dashboard.html')
