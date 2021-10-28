from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class calculate(View):

    def get(self, request, num1, num2, *args, **kwargs):
    
        return HttpResponse(f'{num1} + {num2} = {num1 + num2}')
