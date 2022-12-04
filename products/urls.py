from django.urls import path
from . import views

urlpatterns = [
   
    path('product/<slug>/' , views.get_product , name="get_product"),
]