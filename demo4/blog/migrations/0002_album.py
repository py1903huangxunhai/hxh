# Generated by Django 2.2.2 on 2019-06-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('pic', models.ImageField(upload_to='img')),
            ],
        ),
    ]
