from django.urls import path
from . import views
app_name = 'hospital'
urlpatterns = [
    path('register/',views.hospital_register),
    path('dashboard/',views.dashboard , name='dashboard'),
]