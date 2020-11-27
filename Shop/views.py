from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, request
from django.shortcuts import get_object_or_404

from .models import Product, Cart


class ProductViewAdd(View):
    def get(self, request):
        params = request.GET
        product = Product(name=params['name'], type=params['type'])

        product.price = 10
        product.price_discount = 10

        try:
            product.save()


        except Exception as error:

            return HttpResponse(f"Product and type create error !")

        return HttpResponse(f"Product {params['name']} and type {product.get_type_display()} create successful!")


class ProductView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk = pk)
        return HttpResponse(product.get_type_display())

class ProductViewAll(View):
    def get(self, request):
        product = Product.objects.all()
        return HttpResponse(product)

class CartView(View):
    def get(self, request):
        email = request.GET['email']
        cart = Cart.objects.filter(user__email=email).order_by('-create_at')
        return HttpResponse(cart)




