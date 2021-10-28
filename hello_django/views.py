from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.urls import reverse

class Home(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context
    
    def get_context(self, request, *args, **kwargs):
        return redirect(reverse('calc', kwargs={'num1': 40, 'num2': 2}))
