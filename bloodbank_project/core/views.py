from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blood_stock(request):
    html = """ <h1> BLOOD STOCK </h1>
             <table border = 1>
                 <tr>
                    <th> Blood Group </th>
                    <th> Units Available </th>
                 </tr>
                 <tr>
                    <th>A+ </th>
                    <th>5 </th>
                 </tr>
                 <tr>
                    <th> B+ </th>
                    <th> 7</th>
                 </tr>
                 <tr>
                    <th> O+ </th>
                    <th>12 </th>
                 </tr>
            </table>
            <p> <a href="/">Back To Home Page</a></p>

                      """
    return HttpResponse(html)
    
    
    