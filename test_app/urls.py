from django.urls import path
from . import views
from .views import hello



urlpatterns = [
    path('hello/', hello.as_view()),
]



