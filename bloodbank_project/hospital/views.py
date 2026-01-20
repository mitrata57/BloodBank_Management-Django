from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hospital_register(request):
    html = """
           <h1> Hospital Registration Page </h1>
            <p> Registration Form Coming Soon </p>
           """
    return HttpResponse(html)
