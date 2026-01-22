from django.urls import path
from . import views
app_name = 'donor' 
urlpatterns = [
    path('register/',views.donor_register),
    path('dashboard/',views.dashboard , name='dashboard')
]