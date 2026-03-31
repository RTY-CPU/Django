from django.shortcuts import render,redirect
from . import models
# Create your views here.


# 首页
def home(request):

    return render(request,'home.html')

# 图书列表
def book_list(request):
    #查询所有的图书列表
    book_queryset = models.Book.objects.all()

    return render(request,'book_list.html',locals())

#图书添加
def book_add(request):
    #查询作者
    author_queryset = models.Author.objects.all()
    #查询所有出版社
    publish_queryset = models.Publish.objects.all()
    #提交
    if request.method == 'POST':
        #标题
        title = request.POST.get('title')
        #价格 - 转换为 Decimal
        price = request.POST.get('price')
        #出版日期 - 字符串格式直接传入
        pub_date = request.POST.get('pub_date')
        
        #出版社
        publish_id = request.POST.get('publish')
        #作者 id 因为有多个值 要用列表
        author_ids = request.POST.getlist('author')
        
        #保存到数据库
        book_obj = models.Book.objects.create(
            title = title,
            price = price,
            pub_date = pub_date,
            publish_id = publish_id,
        )
        #保存到第三张表中
        # create() 会创建对象返回
        # add() 可以传入多个值 *将列表数据打散成位置参数 [1,2,3]
        book_obj.authors.add(*author_ids)
        return redirect('book_list')
    return render(request,'book_add.html',locals())

#图书编辑
def book_edit(request,edit_id):

    #根据id查询图书对象
    #select * from app01_book where id = ？
    book_obj = models.Book.objects.filter(pk=edit_id).first()
    #查询所有的作者
    author_queryset  = models.Author.objects.all()
    #查询所有的出版社
    publish_queryset= models.Publish.objects.all()

    if request.method == 'POST':
        # 标题
        title = request.POST.get('title')
        # 价格
        price = request.POST.get('price')
        # 出版时间
        pub_date = request.POST.get('pub_date')
        # 出版社
        publish_id = request.POST.get('publish')
        # 作者 id 因为有多个值 要用列表
        author_ids = request.POST.getlist('author')


        #修改图书表
        #book_obj 是用来调出图书表里的对象（sql表里的键）
        book_obj.title = title
        book_obj.price = price
        book_obj.pub_date = pub_date
        book_obj.publish_id = publish_id

        #修改第三张表
        #set() 必须要传入可迭代对象
        book_obj.authors.set(author_ids)
        #执行修改
        book_obj.save()

        return redirect('book_list')

    return render(request,'book_edit.html',locals())
#删除图书
def book_delete(request,delete_id):

    #根据id删除
    models.Book.objects.filter(pk=delete_id).delete()
    return redirect('book_list')


#-----------------------------出版社----------------------------------------
#出版社列表
def publish_list(request):
    #查询所有的出版社列表
    publish_list = models.Publish.objects.all()
    return render(request,'publish_list.html',locals())

#出版社添加
def publish_add(request):

    if request.method == 'POST':
        #名称
        name = request.POST.get('name')
        #地址
        address = request.POST.get('address')
        #邮箱
        email = request.POST.get('email')
        #保存到数据库
        models.Publish.objects.create(
            name = name,
            address = address,
            email = email
        )
        return redirect('publish_list')
    return render(request,'publish_add.html',locals())
#出版社编辑
def publish_edit(request,publish_id):

    #根据id查询出版社对象
    publish_obj = models.Publish.objects.filter(pk=publish_id).first()

    if request.method == 'POST':
        #名称
        name = request.POST.get('name')
        #地址
        address = request.POST.get('address')
        #邮箱
        email = request.POST.get('email')
        #修改
        publish_obj.name = name
        publish_obj.address = address
        publish_obj.email = email
        #保存
        publish_obj.save()
        #跳转
        return redirect('publish_list')
    return render(request,'publish_edit.html',locals())

#出版社删除
def publish_delete(request,delete_id):
    #根据id删除
    models.Publish.objects.filter(pk=delete_id).delete()
    return redirect('publish_list')


#----------------------------作者----------------------------------------
##作者列表
def author_list(request):
    #查询所有的作者列表
    author_list = models.Author.objects.all()

    return render(request,'author_list.html',locals())

##增加作者
def author_add(request):

    if request.method == 'POST':
        # 姓名
        name = request.POST.get('name')
        # 年龄
        age = request.POST.get('age')
        # 电话
        phone = request.POST.get('phone')
        # 地址
        addr = request.POST.get('addr')

        #因为要添加两张表 要先拿到主表的对象（1对1）
        author_obj = models.Author.objects.create(name=name,age=age)
        #先添加作者后添加详情
        models.AuthorDetail.objects.create(
            phone = phone,
            addr = addr,
            author = author_obj
        )
        #跳转作者列表
        return redirect('author_list')

    return render(request,'author_add.html',locals())

# 编辑作者
def author_edit(request,author_id):

    # 根据id查询出版社对象
    author_obj = models.Author.objects.filter(pk=author_id).first()

    if request.method == 'POST':
        # 名称
        name = request.POST.get('name')
        # 年龄
        age = request.POST.get('age')
        # 地址
        addr = request.POST.get('addr')
        # 电话
        phone = request.POST.get('phone')

        # 修改
        author_obj.name = name
        author_obj.age = age
        # 保存
        author_obj.save()
        #详情表
        author_obj.authordetail.phone = phone
        author_obj.authordetail.addr =addr
        author_obj.authordetail.save()

        # 跳转
        return redirect('author_list')


    return render(request,'author_edit.html',locals())

#删除作者
def author_delete(request,delete_id):
    models.Author.objects.filter(pk=delete_id).delete()
    return redirect('author_list')