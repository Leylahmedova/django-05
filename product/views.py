from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Blog
from .forms import BlogForm
# from django.db.models import F,FloatField,ExpressionWrapper
# from django.db.models.functions import Coalesce
# Create your views here.

def product_list_view(request):
    blogs=Blog.objects.all()
    return render(request,'list.html',{'blogs':blogs})

def product_detail_view(request,id):
    blogs=Blog.objects.all()
    text={
        "id":id,
        "blogs":blogs

    }
    return render(request,'detail.html',text)

def product_create_view(request):
    form=BlogForm()
    
    if request.method == "POST":
        form=BlogForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("list")


    text={
        "form":form
    }
    return render(request,"create.html",text)

def product_update_view(request,id):
    
    blog=get_object_or_404(Blog,id=id)
    form=BlogForm(instance=blog)
    
    if request.method == "POST":
        form=BlogForm(request.POST,instance=blog)

        if form.is_valid():
            form.save()

            return redirect("list")


    text={
        "form":form
    }
    return render(request,"update.html",text)



def product_delete_view(request,id):
    
    blog=get_object_or_404(Blog,id=id)
    form=BlogForm(instance=blog)
    
    if request.method == "POST":
        form=BlogForm(request.POST)

        # if form.is_valid():
        blog.delete()

        return redirect("list")


    text={
        "form":form
    }
    return render(request,"delete.html",text)
