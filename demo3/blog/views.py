from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import View,ListView,DetailView
from .models import *
from comments.forms import CommentForms
# Create your views here.

class IndexView(View):
    """
    文章列表页视图类
    """
    def get(self,req):
        """
        重写get请求
        :param req:
        :return:
        """
        articles =Article.objects.all()
        return render(req,"blog/index.html",locals())

# class IndexView(View):
#     def get(self,req):
#         return render(req,"blog/index.html")

class SingleView(View):
    """
    文章详情页视图
    """
    def get(self,req,id):
        """
        重写get请求
        :param req:
        :param id:  文章id
        :return:
        """
        article = Article.objects.get(pk=id)
        cf=CommentForms()
        return render(req,"blog/single.html",locals())

    def post(self,req,id):
        cf=CommentForms(req.POST)
        if cf.is_valid():
            # 暂时不保存数据库
            res=cf.save(commit=False)
            res.article=get_object_or_404(Article,pk=id)
            # 给评论表中的文章赋值后才可以保存
            res.save()
            return redirect(reverse('blog:single',args=(id,)))
