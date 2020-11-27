from django.shortcuts import render, redirect, reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage

from .settings.info import INFO


class IndexView(View):
    def get(self, request):

        contex = {}
        contex.update(INFO)
        return render(request, 'hi/index.html', contex)

class ShopView(View):
    def get(self, request, page=1):
        products_list = [
            {
                'name': 'Bell Pepper',
                'image': 'hi/images/product-1.jpg',
                'price': '$150.00',
                'discount': '30%',
                'price_sale': '$100.00'
            },
            {
                'name': 'Strawberry',
                'image': 'hi/images/product-2.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Green Beans',
                'image': 'hi/images/product-3.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Purple Cabbage',
                'image': 'hi/images/product-4.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Tomatoe',
                'image': 'hi/images/product-5.jpg',
                'price': '$120.00',
                'discount': '30%',
                'price_sale': '$80.00'
            },
            {
                'name': 'Brocolli',
                'image': 'hi/images/product-6.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Carrots',
                'image': 'hi/images/product-7.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Fruit Juice',
                'image': 'hi/images/product-8.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Onion',
                'image': 'hi/images/product-9.jpg',
                'price': '$120.00',
                'discount': '30%',
                'price_sale': '$80.00'
            },
            {
                'name': 'Apple',
                'image': 'hi/images/product-10.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Garlic',
                'image': 'hi/images/product-11.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Chilli',
                'image': 'hi/images/product-12.jpg',
                'price': '$120.00'
            }
        ]

        product_on_page = 999
        paginator = Paginator(products_list, product_on_page)



        try:
            products_list = paginator.page(page)
            products_list.page_tuple = tuple(paginator.page_range)
        except EmptyPage:
            return redirect(reverse('shop'))

        contex = {'page_obj': products_list}
        contex.update(INFO)
        return render(request, 'hi/shop.html', contex)

# Create your views here.
