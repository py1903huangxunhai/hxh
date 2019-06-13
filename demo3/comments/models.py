from django.db import models
from blog.models import Article
# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now=30)
    content = models.CharField(max_length=500)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
