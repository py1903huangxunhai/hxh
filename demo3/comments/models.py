from django.db import models
from blog.models import Article
# Create your models here.
class Comment(models.Model):
    """
    评论表：与文章表存在多对一关系
    name：评论人
    create_time : 评论时间
    content: 评论内容
    article：文章
    """
    name = models.CharField(max_length=30,verbose_name='姓名')
    create_time = models.DateTimeField(auto_now=30)
    content = models.TextField(max_length=500,verbose_name='评论内容')
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    email=models.EmailField(blank=True,null=True,verbose_name='邮箱')
    url=models.CharField(blank=True,null=True,max_length=20,verbose_name='网址')

    def __str__(self):
        return self.name
