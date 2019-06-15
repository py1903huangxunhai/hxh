from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import View,ListView,DetailView
from .models import *
from comments.forms import CommentForms
from comments.models import Comment
from django.http import HttpResponse
from django.core.paginator import Paginator
import markdown
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
        articles = Article.objects.all()
        # latestarticles = articles.order_by("-create_time")[:3]

        # # 得到分页
        # paginator = Paginator(articles,2)
        # print(paginator.count)
        # print(paginator.object_list)
        # print(paginator.num_pages)
        # print(paginator.page_range)
        # # 得到页面
        # page = paginator.get_page(2)
        # print(page.object_list)
        # # 由页面得到分页    分页可以得到页面  页面可以得到分页
        # print(page.paginator)
        # print(page.number)
        # print(paginator is page.paginator)


        paginator = Paginator(articles,1)
        pagenum = req.GET.get("page")
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = "/"
        return render(req,"blog/index.html",{"page":page})
        # return render(req,"blog/index.html",locals())


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
        # article = Article.objects.get(pk=id)
        article = get_object_or_404(Article, pk=id)

        # 1获取markdown实例
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        # 2 使用markdown实例渲染指定字段
        article.body = md.convert(article.body)
        # 3 将md的目录对象赋予 article
        article.toc = md.toc

        # 向详情页面传递一个评论表单
        cf = CommentForms()
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

        paginator = Paginator(articles,1)
        pagenum = req.GET.get("page")
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = "/archives/%s/%s/" % (year,month)
        return render(req, "blog/index.html", {"page":page})

class CategoryView(View):
    def get(self,req,id):
        category = get_object_or_404(Category,pk=id)
        articles = category.article_set.all()
        paginator = Paginator(articles, 1)
        pagenum = req.GET.get("page")
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = "/category/%s/" % (id,)
        return render(req, "blog/index.html", locals())

class TagView(View):
    def get(self,req,id):
        tag = get_object_or_404(Tag,pk=id)
        articles = tag.article_set.all()
        paginator = Paginator(articles, 1)
        pagenum = req.GET.get("page")
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = "/tags/%s/" % (id,)
        return render(req, "blog/index.html", locals())
