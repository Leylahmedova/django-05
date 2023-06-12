
from django.contrib import admin
from django.urls import path
from product.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("list/",product_list_view,name='list'),
    # path("newlist/",product_newlist_view,name='newlist'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
