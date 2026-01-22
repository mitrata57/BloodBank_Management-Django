from django.contrib import admin
from django.urls import path, include
# bloodbank_project/urls.py
print("PROJECT URLS LOADED")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),           
    path('accounts/', include('accounts.urls')),  # /accounts/register, /accounts/login
    path('donor/', include('donor.urls')),
    path('receiver/', include('receiver.urls')),
    path('hospital/', include('hospital.urls')),
]