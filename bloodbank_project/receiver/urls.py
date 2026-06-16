from django.urls import path
from . import views

app_name = 'receiver'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('request/', views.create_request, name='create_request'),
    path('history/', views.request_history, name='request_history'),
]