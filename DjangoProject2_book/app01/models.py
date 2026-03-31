from django.db import models

# Create your models here.


class Book(models.Model):
    # 书名
    title = models.CharField(max_length=33)
    # 价格
    price = models.DecimalField(max_digits=7,decimal_places=2)
    # 出版社日期
    pub_date = models.DateField(auto_now_add=False)

    # 建立关系 图书和出版社是一对多的关系
    # 创建之后 会自动关联 publish的主键字段
    # 同时创建的字段名后面会加上_id 变为publish_id
    publish = models.ForeignKey(to='Publish',on_delete=models.CASCADE)
    #图书和作者是多对多的关系
    authors = models.ManyToManyField(to='Author')


class Publish(models.Model):
    # 出版社名称
    name = models.CharField(max_length=32)
    # 地址
    address = models.CharField(max_length=64)
    #出版社邮箱
    email = models.EmailField()

class Author(models.Model):
    # 作者姓名
    name = models.CharField(max_length=32)
    # 作者年龄
    age = models.IntegerField()

class AuthorDetail(models.Model):
   #手机号
   phone = models.BigIntegerField()
   #地址
   addr = models.CharField(max_length=64)
   #一对一
   author = models.OneToOneField(to='Author',on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=33)
    age = models.IntegerField()

    #以元组套元组的形式 - 枚举列出所有的可能性
    #参数： 第一个值是存储到数据库的值 第二个值是对应的值
    gender_choices = (
        (1,'hh'),
        (2,'帅'),
        (3,'???'),
    )

    gender = models.IntegerField(choices=gender_choices)