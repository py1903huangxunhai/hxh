from django.conf.urls import url
from .views import index,list,detail,deletehero,deletebook,addhero,addbook
app_name = 'booktest'

urlpatterns = [

    url(r'^list/$',list,name = 'list'),
    #通过正则表达式传递参数，通过（）分组传参，视图函数一个分组，需要有一个形参
    url(r'^detail/(\w+)/$',detail,name = 'detail'),
    url(r'^$',index,name = 'index'),


    # 角色相关
    url(r'^deletehero/(\d+)/$',deletehero,name="deletehero"),
    #添加英雄
    url(r'^addhero/(\d+)/$',addhero,name='addhero'),

    #书籍相关
    url(r'^deletebook/(\d+)/$',deletebook,name="deletebook"),
    #添加书籍
    url(r'^addbook/$',addbook,name='addbook')
]