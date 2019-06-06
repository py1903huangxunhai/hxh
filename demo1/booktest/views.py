from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import BookInfo,HeroInfo
from django.template import loader

'''
MVT中的 V 编写视图
'''
# Create your views here.

def index(req):
    # print(req.headers["User-Agent"])
    # return HttpResponse('这里是首页啊')
    # 1.获取模板
    # temp = loader.get_template("booktest/index.html")
    # # 2使用模板渲染动态数据
    # res = temp.render({"username":"hxh","age":"20"})
    # # 3返回渲染结果
    # return HttpResponse(res)
    return render(req, "booktest/index.html",{"username":"hxh","password":"********"})


def list(req):
    books = BookInfo.objects.all()

    # return HttpResponse("这里是列表页哦")

    # temp = loader.get_template("booktest/list.html")
    # res = temp.render({"book":books})
    # return HttpResponse(res)
    return render(req, "booktest/list.html",{"book":books})

# def detail(req,id,num):
#     return HttpResponse('detail网页,%s,%s' % (id,num))

def detail(req,id):
    book = BookInfo.objects.get(pk=id)

    # return HttpResponse('这里是%s的详情页' % book.title)

    # temp = loader.get_template("booktest/detail.html")
    # res = temp.render({"book":book})
    # return HttpResponse(res)
    return render(req, "booktest/detail.html",{"book":book})

def deletehero(req,id):
    hero = HeroInfo.objects.get(pk=id)
    hero.delete()


    return HttpResponseRedirect("/detail/%s/" % (hero.book.id,))
    # return HttpResponse("删除了%s" % (id,))


#添加英雄函数
def addhero(req,id):
    book=BookInfo.objects.get(pk=id)
    if req.method=='GET':
        return render(req,'booktest/addhero.html',{'book':book})
    elif req.method=='POST':
        hero=HeroInfo()
        hero.name=req.POST.get('heroname')
        hero.content=req.POST.get('herocontent')
        hero.book=book
        hero.save()
        return HttpResponseRedirect('/detail/%s/'%(id,))