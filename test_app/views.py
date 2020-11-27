from django.shortcuts import render

from django.views import View
from django.http import HttpResponse

class hello(View):
    def get(self, request):
        text = "<h1>Hello world!</h1>"
        return HttpResponse(text)

# Create your views here.
