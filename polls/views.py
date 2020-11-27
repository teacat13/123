from django.shortcuts import render
from datetime import datetime
from django.views import View
import random
from django.http import HttpResponse
from django.shortcuts import render

class CurrentDateView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)
class randoms(View):
    def get(self, request):
        rand = random.randint(1, 10000)
        return HttpResponse(rand)
class IndexView(View):
    def get(self, request):
        return render(request, "polls/index.html", {'first_name': 'John', 'last_name': 'Doe'})






# Create your views here.
