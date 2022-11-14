from django.contrib import admin
from django.urls import path, include, re_path
from n_api.api import api


urlpatterns = [
   path('drf_api/', include('drf_api.urls')),
   path('ninja_api/', api.urls),
]
