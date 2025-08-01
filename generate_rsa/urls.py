from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_rsa_key, name='generate_rsa_key'),
]