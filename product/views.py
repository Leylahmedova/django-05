from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Product,ProductImage
from django.db.models import F,Q
# from .forms import ProductForm
# from django.db.models import F,FloatField,ExpressionWrapper
# from django.db.models.functions import Coalesce
# Create your views here.

# def product_list_view(request):
#     products=Product.objects.annotate(total_price=F("price")-F("discount_price"))
#     return render(request,'list.html',{'products':products})

# def product_newlist_view(request):
#     products=Product.objects.annotate(total_price=F("price")-F("discount_price"))
#     return render(request,'newlist.html',{'products':products})


def product_list_view(request):
    products=ProductImage.objects.all()
    return render(request,'list.html',{'products':products})
