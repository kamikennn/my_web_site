from django.shortcuts import render
from django.views.generic import TemplateView

class AboutmeView(TemplateView):
    template_name='aboutme.html'