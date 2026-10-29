from django.urls import path
from .views import create_short_url, redirect_to_url

urlpatterns = [
    path('<slug:code>', redirect_to_url),
    path('', create_short_url),
]
