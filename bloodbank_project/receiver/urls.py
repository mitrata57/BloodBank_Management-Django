from django.urls import path
from . import views
app_name = 'receiver' 
urlpatterns = [
    path('register/',views.receiver_register),
    path('dashboard/',views.dashboard , name='dashboard')
]