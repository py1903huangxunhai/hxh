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
        # latestarticles = articles.order_by("-create_time")[:3]
        return render(req,"blog/index.html",locals())


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

        # latestarticles = Article.objects.all().order_by("-create_time")[:3]

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


class ArchieveView(View):
    def get(self,req,year,month):
        articles = Article.objects.filter(create_time__year = year, create_time__month = month)
        return render(req, "blog/index.html", locals())

class CategoryView(View):
    def get(self,req,id):
        category = get_object_or_404(Category,pk=id)
        articles = category.article_set.all()
        return render(req, "blog/index.html", locals())

class TagView(View):
    def get(self,req,id):
        tag = get_object_or_404(Tag,pk=id)
        articles = tag.article_set.all()
        return render(req, "blog/index.html", locals())
