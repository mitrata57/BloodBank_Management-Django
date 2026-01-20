from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
     
     html = """
                   <h1>Welcome to Blood Bank Management System</h1>
                   <p>Save lives by donating or requesting blood</p>
                    <ul>
                        <li><a href="/blood-stock/">View Available Blood Stock</a></li>
                        <li><a href="/donor/register/">Register as Donor</a></li>
                        <li><a href="/receiver/register/">Register as Receiver</a></li>
                        <li><a href="/hospital/register/">Register as Hospital</a></li>
                        <li><a href="/about/">About Page</a></li>
                    </ul>
    """
     return HttpResponse(html)


def about(request):
    
    html = """
    <h1>About Blood Bank Management System</h1>
    <p>We connect blood donors with recipients to save lives.</p>
    <h2>How It Works:</h2>
    <ul>
        <li><b>Donors:</b> Register, donate blood, save lives</li>
        <li><b>Receivers:</b> Request blood when needed</li>
        <li><b>Hospitals:</b> Manage inventory and requests</li>
    </ul>
    <p><b>Key Feature:</b> You can be both a donor AND receiver!</p>
    <p><a href="/">Back to Home</a></p>
    """
    return HttpResponse(html)
 
   
   
