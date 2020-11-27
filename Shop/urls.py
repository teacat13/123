from django.urls import path
from .views import ProductViewAdd
from . import views
from .views import ProductView
from .views import ProductViewAll
from .views import CartView
urlpatterns = [
    path('product/add', ProductViewAdd.as_view()),
    path('product/<int:pk>', ProductView.as_view()),
    path('product/', ProductViewAll.as_view()),
    path('cart/', CartView.as_view()),
]