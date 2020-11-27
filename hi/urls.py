from django.urls import path
from . import views
from .views import IndexView
from .views import ShopView




urlpatterns = [

    path('hi/', IndexView.as_view()),
    path('shop/', ShopView.as_view(), name='shop'),
]