
from django.contrib import admin
from django.urls import path
from product.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path("list/",product_list_view),
    path("detail/<int:id>/",product_detail_view)
]
