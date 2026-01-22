from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def receiver_register(request):
    return HttpResponse("<h1> Receiver Registration Page </h1>")

def dashboard(request):
    return render(request ,'receiver/dashboard.html')