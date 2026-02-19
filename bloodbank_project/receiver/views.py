from django.shortcuts import render
from django.http import HttpResponse
from accounts.decorators import receiver_required

def receiver_register(request):
    return HttpResponse("<h1> Receiver Registration Page </h1>")

@receiver_required
def dashboard(request):
    return render(request, 'receiver/dashboard.html')