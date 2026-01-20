from django.urls import path
from . import views

urlpatterns = [
    path('blood-stock/', views.blood_stock, name='blood_stock'),
]