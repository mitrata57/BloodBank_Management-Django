from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.donor_register),
]