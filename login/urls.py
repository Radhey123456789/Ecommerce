from django.conf.urls import include,url
from .views import *

urlpatterns = [
    
    url(r'^$', user_register,name='user_register'),
    url(r'^user_login/$', user_login, name='user_login'),
    
    ]                  
