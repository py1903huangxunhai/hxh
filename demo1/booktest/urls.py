from django.conf.urls import url
from .views import index,list,detail

urlpatterns = [
    url('index/',index),
    url('list/',list),
    url(r'^detail/(\w+)/$',detail)
]