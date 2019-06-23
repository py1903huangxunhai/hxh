from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import View,ListView,DetailView
from .models import *

# Create your views here.

# def index(req):
#     return HttpResponse("这里是首页")
#
# def list(req):
#     return HttpResponse("这里是列表页")

class IndexView(View):
    """
    文章列表视图类
    """
    def get(self,req):
        categorys = Category.objects.all()
        articles = categorys[0].article_set.all()

        return render(req, "blog/index.html",locals())

class DetailsView(View):
    """
    文章详情视图类
    """
    def get(self,req,id):
        article = get_object_or_404(Article,pk=id)
        return render(req, "blog/details.html",locals())

class CategoryView(View):
    """
    分类视图
    """
    def get(self,req,id):
        categorys = Category.objects.all()
        category = get_object_or_404(Category,pk=id)

        articles = category.article_set.all()
        return render(req,'blog/index.html',locals())

class WhisperView(View):
    """
    微语
    """
    def get(self,req):
        return render(req,'blog/whisper.html',locals())


class AlbumView(View):
    """
    相册
    """
    def get(self,req):
        als = Album.objects.all()

        return render(req,'blog/album.html',locals())

class LeacotsView(View):
    """
    留言
    """
    def get(self,req):
        return render(req, 'blog/leacots.html', locals())

class AboutView(View):
    """
    关于
    """
    def get(self,req):
        return render(req, 'blog/about.html', locals())