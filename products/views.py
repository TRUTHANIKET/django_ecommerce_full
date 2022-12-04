
from django.shortcuts import render
from products.models import Product
from . import views
from django.contrib.auth.decorators import login_required




@login_required
def get_product(request , slug):
    try:
        product = Product.objects.get(slug =slug)
        return render(request  , 'home/product_detail.html' , context = {'product' : product})

    except Exception as e:
        print(e)