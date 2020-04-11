from django.shortcuts import render
from django.views.generic import TemplateView

class StrengthView(TemplateView):
    template_name='strength.html'