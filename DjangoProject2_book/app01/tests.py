from django.test import TestCase

import os


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject2_book.settings')
    import django
    django.setup()

    from app01 import models

    res = models.User.objects.filter(pk=1).first()
    #直接对象输出 属性可以直接返回
    print(res)
    #获取对应数据,固定写法:get_字段名_display()
    print(res.get_gender_display())

    #如果不存在呢
    res = models.User.objects.filter(pk=4).first()
    ##直接对象输出 属性可以直接返回
    print(res)
    #获取对应数据,固定写法:get_字段名_display()
    print(res.get_gender_display())
