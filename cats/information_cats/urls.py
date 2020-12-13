from django.urls import path 
from .views import cat

urlpatterns = [
        path('cat', cat, name='cats')
        ]
