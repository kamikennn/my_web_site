from django.urls import path 
from .views import StrengthView

urlpatterns = [
    path('',StrengthView.as_view(),name='strength'),
]