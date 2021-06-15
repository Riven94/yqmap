from django.db import models

# Create your models here.

class User(models.Model): #创建用户信息表
    name=models.CharField(max_length=30,verbose_name='姓名')
    ways=models.CharField(max_length=50,verbose_name='走过的省份')
    days = models.CharField(max_length=50, verbose_name='日期')

class City(models.Model): #创建城市信息表
    city=models.CharField(max_length=24,verbose_name='省份')
    nums=models.CharField(max_length=24,verbose_name='确诊数')

class NewsPost(models.Model):
    title = models.CharField(max_length = 150)  # 新闻标题
    body = models.TextField()                   # 新闻正文
    timestamp = models.DateTimeField()          # 创建时间