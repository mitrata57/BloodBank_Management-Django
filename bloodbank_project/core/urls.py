from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('blood-stock/', views.blood_stock, name='blood_stock'),
    path('about/', views.about, name='about'),
]