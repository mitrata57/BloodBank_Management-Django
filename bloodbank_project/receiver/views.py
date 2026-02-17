from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def receiver_register(request):
    return HttpResponse("<h1> Receiver Registration Page </h1>")

@login_required(login_url='accounts:login')
def dashboard(request):
    return render(request ,'receiver/dashboard.html')