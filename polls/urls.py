from django.urls import path
from . import views
from .views import CurrentDateView
from .views import  randoms
from .views import IndexView

urlpatterns = [
    path('random/', randoms.as_view()),
    path('datetime/', CurrentDateView.as_view()),
    path('', IndexView.as_view()),
]



