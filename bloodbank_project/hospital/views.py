from django.shortcuts import render


# Create your views here.
def hospital_register(request):
    return render(request, 'hospital/register,html')

def dashboard(request):
    return render(request, 'hospital/dashboard.html')
