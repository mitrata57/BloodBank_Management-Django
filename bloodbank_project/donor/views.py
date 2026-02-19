from django.shortcuts import render
from django.http import HttpResponse
from accounts.decorators import donor_required

def donor_register(request):
    return HttpResponse("<h1> Donor Registration Page </h1>")

@donor_required
def dashboard(request):
    context = {
        'total_donations': 0,     
        'next_eligible': 'N/A',   
        'lives_saved': 0,          
    }
    return render(request, 'donor/dashboard.html', context)