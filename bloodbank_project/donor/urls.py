from django.urls import path
from . import views

app_name = 'donor'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('donate/', views.record_donation, name='record_donation'),
    path('history/', views.donation_history, name='donation_history'),
]