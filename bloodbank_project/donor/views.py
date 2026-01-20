from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def donor_register(request):
    return HttpResponse("<h1> Donor Registration Page </h1>")
