from django.urls import path
from .views import SignUpView

urlpatterns = [
    #/guests/signup/
    path('signup/', SignUpView.as_view(), name='signup'),
] 