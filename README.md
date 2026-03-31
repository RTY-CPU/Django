[PROJECT_INTRO.md](https://github.com/user-attachments/files/26371494/PROJECT_INTRO.md)
# Django图书管理系统 - 项目介绍

这是一个基于Django 5.2.12框架开发的完整图书管理系统,采用经典的MVC架构,实现了图书、出版社和作者的全生命周期管理。

## 核心功能模块

### 1. 图书管理
- 图书列表展示(支持关联查询出版社和作者)
- 图书添加(支持多对多作者关联)
- 图书编辑(更新图书及作者关系)
- 图书删除(级联删除操作)

### 2. 出版社管理
- 出版社列表展示
- 出版社信息增删改查
- 地址、邮箱等联系信息管理

### 3. 作者管理
- 作者基本信息管理(姓名、年龄)
- 作者详情管理(电话、地址)
- 一对一关系维护

## 技术架构

- **后端框架**: Django 5.2.12
- **数据库**: MySQL 5.7+
- **前端技术**: Bootstrap 3.4.1 + jQuery 3.7.0
- **数据库配置**: 使用MySQL数据库,名称为`django_book`

## 数据库模型设计

项目包含5个核心模型:

### Book(图书)
- 图书名称、价格、出版日期
- 关联出版社(一对多)和作者(多对多)

### Publish(出版社)
- 名称、地址、邮箱

### Author(作者)
- 姓名、年龄

### AuthorDetail(作者详情)
- 手机号、地址,与作者一对一关联

### User(用户)
- 用户名、年龄、性别(扩展测试用)

## 项目特色

1. **完整的CRUD操作**: 实现了所有增删改查功能
2. **关系型数据处理**: 正确处理了一对多、多对多、一对一关系
3. **响应式界面**: 使用Bootstrap框架实现响应式布局
4. **URL路由设计**: 使用正则表达式实现RESTful风格的URL
5. **模板复用**: 基础模板继承,提高代码复用性

## 项目结构

```
DjangoProject2_book/
├── DjangoProject2_book/      # 项目配置
│   ├── settings.py          # Django配置文件
│   ├── urls.py              # URL路由配置
│   └── wsgi.py              # WSGI配置
├── app01/                    # 主应用
│   ├── models.py            # 数据模型
│   ├── views.py             # 视图逻辑
│   └── admin.py             # 管理后台
├── templates/               # HTML模板
│   ├── book_*.html         # 图书相关模板
│   ├── publish_*.html      # 出版社相关模板
│   └── author_*.html       # 作者相关模板
├── static/                  # 静态资源
│   ├── bootstrap/          # Bootstrap框架
│   └── js/                 # jQuery库
└── manage.py               # 管理脚本
```

## 运行方式

```bash
# 安装依赖
pip install django

# 数据库迁移
python manage.py makemigrations
python manage.py migrate

# 启动开发服务器
python manage.py runserver

# 访问地址
http://localhost:8000
```

## 学习价值

这是一个适合Django初学者学习的完整项目,涵盖了Django开发的核心概念,包括:
- ORM操作
- 视图处理
- 模板渲染
- URL路由
- 表单处理
- 关系型数据库设计

---

**项目位置**: `c:\Users\lenovo\Desktop\DjangoProject2_book`  
**创建日期**: 2026-03-31
