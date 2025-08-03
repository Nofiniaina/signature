from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_document, name='sign_document'),
]