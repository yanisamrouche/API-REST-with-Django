
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('drf_api/', include('drf_api.urls')),
]
