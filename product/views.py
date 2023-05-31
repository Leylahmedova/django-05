from django.shortcuts import render,HttpResponse
from .models import Product
from django.db.models import F,FloatField,ExpressionWrapper
from django.db.models.functions import Coalesce
# Create your views here.

def product_list_view(request):
    products=Product.objects.annotate(
        total_price=Coalesce(F('price')-F('discount_price'),0,output_field=FloatField())
    )
    return render(request,'list.html',{'products':products})

def product_detail_view(request,id):
    products=Product.objects.annotate(
        total_price=Coalesce(F('price')-F('discount_price'),0,output_field=FloatField())
    )
    text={
        "id":id,
        "products":products

    }
    return render(request,'detail.html',text)

def product_create_view(request):
    text={

    }
    return render(request,"create.html",text)
