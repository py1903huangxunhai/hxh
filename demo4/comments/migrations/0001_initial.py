# Generated by Django 2.2.2 on 2019-06-20 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(max_length=500, verbose_name='评论内容')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('url', models.CharField(blank=True, max_length=20, null=True, verbose_name='网址')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
        ),
    ]
