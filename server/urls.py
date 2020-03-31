from django.urls import path
from .views import *

app_name = 'server'

urlpatterns = [
    path('upload/', VahanView.as_view(), name='question'),
    path('<str:pk>/', VahanDetailView.as_view(), name='question'),
]