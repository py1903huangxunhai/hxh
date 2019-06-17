"""
自定义标签

"""

from django.template import Library
from ..models import Article,Category,Tag,Ads
register = Library()

@register.simple_tag
def getlatestarticles(num=3):
    """
    得到最新的文章
    :param num:
    :return:
    """
    return Article.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def getarchives():
    # result = Article.objects.dates("create_time","month")
    # return result
    return Article.objects.dates("create_time","month")

@register.simple_tag
def getcategorys():
    return Category.objects.all()

@register.simple_tag
def gettags():
    return Tag.objects.all()

@register.simple_tag
def getads():
    return Ads.objects.all()