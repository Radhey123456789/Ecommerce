from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
	url(r'^category/(\w+)/$',product_category,name='category'),
	url(r'^detail/(\d+)/$',detail,name='detail'),
	
	url(r'^cartinfo/$', cart_detail,name='cartinfo'),
	url(r'^cartinfo/(\d+)/$', delete_product,name='delete_product'),
]
