from django.urls import path 
from .views import AboutmeView

urlpatterns = [
    path('',AboutmeView.as_view(),name='about_me'),
]