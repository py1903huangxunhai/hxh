from django.conf.urls import url
from .views import index,list,detail
app_name = 'booktest'

urlpatterns = [

    url(r'^list/$',list,name = 'list'),
    #通过正则表达式传递参数，通过（）分组传参，视图函数一个分组，需要有一个形参
    url(r'^detail/(\w+)/$',detail,name = 'detail'),
    url(r'^$',index,name = 'index')
]