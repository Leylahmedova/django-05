
from django.contrib import admin
from django.urls import path
from product.views import *
# app_name='mainapp'


urlpatterns = [
    path("admin/", admin.site.urls),
    path("list/",product_list_view,name='list'),
    path("detail/<int:id>/",product_detail_view,name='detail'),
    path("update/<int:id>/",product_update_view,name='update'),
    path("delete/<int:id>/",product_delete_view,name='delete'),
    path('create/',product_create_view,name='create')
]
