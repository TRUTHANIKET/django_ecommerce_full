from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
# Create your views here.
def home(request):
    context={'products':Product.objects.all()}
    return render(request,'home/home.html',context)


# def get_product(request , slug):
#     try:
#         product = Product.objects.get(slug =slug)
#         return render(request  , 'product_detail.html' , context = {'product' : product})

#     except Exception as e:
#         print(e)