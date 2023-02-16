## Django

Django makes it easier to build better web apps more quickly and with less code.



 The framework was named after guitarist Django Reinhardt.



### MVC

Model–view–controller (MVC) is a software architectural pattern

![mvc](data\mvc.jpg)



- Benefit of using MVC
  - https://www.geeksforgeeks.org/benefit-of-using-mvc/



#### MVT

control is handled by the framework itself

![mvt](data\mvt.jpg)





### Virtual environment 

#### anaconda virtual environment

https://www.anaconda.com/

```
conda create -n myenv python=3.8
```

```
conda env list
```

```
conda activate myenv
```

https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment



#### pip virtual environment

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/



### install Django

#### anaconda 

```
conda install -c anaconda django
```

#### pip

```
pip install django
```

#### Version

```
python -m django --version
```

#### after installation

```
# use 'where python' in anaconda prompt
```

- python/environment
  - python.exe
  - Scripts
    - pip.exe
    - django-admin.exe  (Django's command-line utility)
    - ...
  - libs
    - site-packages
      - djangos
      - mysql_connector
      - 
      - ...
    - standard libraries (turtle,csv,...)



### Create a project

https://docs.djangoproject.com/en/4.1/intro/tutorial01/

use `dir` to select the correct directory on a windows operating system

```
dir 
```



```
django-admin startproject mysite
```



```
└───mysite
    │   manage.py			# project management
    │
    └───mysite
            __init__.py
            settings.py			# configuaration
            urls.py			# url-function mapping
            asgi.py			# receive requests
            wsgi.py			# receive requests
```



> - The outer `mysite/` root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
> - `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about `manage.py` in [django-admin and manage.py](https://docs.djangoproject.com/en/4.1/ref/django-admin/).
> - The inner `mysite/` directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. `mysite.urls`).
> - `mysite/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) in the official Python docs.
> - `mysite/settings.py`: Settings/configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/4.1/topics/settings/) will tell you all about how settings work.
> - `mysite/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher](https://docs.djangoproject.com/en/4.1/topics/http/urls/).
> - `mysite/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/) for more details.
> - `mysite/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/) for more details.



### app

a project can contain multiple apps

```
python manage.py startapp app1
```



```
└───mysite
    ├───app1
    │   │   admin.py
    │   │   apps.py
    │   │   models.py	# orm
    │   │   tests.py
    │   │   views.py
    │   │   __init__.py
    │   │
    │   └───migrations
    │           __init__.py
    │ 
    │	manage.py
    │ 
    └───mysite
        │   asgi.py
        │   settings.py
        │   urls.py
        │   wsgi.py
        │   __init__.py
```

### Quick start

#### register apps

`mysite/setting.py`

![register_app](data/register_app.jpg)

#### url -function mapping

`mysite/urls.py`



![url-function](data\url-function.jpg)



#### define functions in views

`app1/views.py`

![url-function](data\function in views.jpg)







#### verify your Django project works

```
python manage.py runserver
```



### Views

![views](data\views.jpg)

- a URL can be connected to a view
- a view can be a function or a class
- a view function needs at least one argument



#### include other `URLconfs`



![include_views](data\include_views.jpg)





#### How does Django find a view?

- receive a url
- try to map the URL to views by using `URLconf` 
  - the entry of `URLconf` is `ROOT_URLCONF` in `mysite/setting.py`
- if a view is found, return the view; otherwise return HTTP 404 Not Found





- http://127.0.0.1:8000/app1/login/ 

  - `mysite/urls.py`:  

    `path('app1/', include('app1.urls')),`

    - `mysite/app1/urls.py`: 

      `path('login/', views.app1_login),`

      - `mysite/app1/views.py`:  

        `def app1_login(request):`

        ​	` return HttpResponse("app1_login")`







### Templates

![template](data\template.jpg)

```
def user(request):
    return render(request, "user.html")
```

`app1/templates/user.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <h1>This is an HTML file</h1>
</head>
<body>
    
</body>
</html>
```





#### How does Django find a template?

1. `TEMPLATES[0][DIRS]` in `setting.py`
   - use `os.path.join(BASE_DIR, 'templates')` for the directory `mysite/templates`
2. `templates` directory of each registered app





### static files

- css
- image
- js

#### How does Django find a static file?

1. `STATICFILES_DIRS`  in `setting.py`
   - add `STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]` for the directory `mysite/static`
2. `static` directory of each registered app
   - make sure`STATIC_URL = '/static/'` in `setting .py`

`cs.html`

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>

    <link rel="stylesheet" href="{% static 'style.css' %}">
    
</head>
<body>
    <h1>This is another HTML file</h1>
    <img src="{% static '/python.jpg' %}" alt="">
</body>
</html>
```

`app1/static/style.css`

```css
h1 {
    color: red;
}
```



### template language

https://docs.djangoproject.com/en/4.1/ref/templates/language/









![templates](data\templates.jpg)



render():

- get HTML files with template language (placeholders)
- replace placeholders with actual values
- generate rendered HTML files



`cs.html`

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>

    <link rel="stylesheet" href="{% static 'style.css' %}">
    
</head>
<body>
    <h1>This is another HTML file</h1>
    <h3>{{ name }}</h3>
    <hr>
    <h3>{{ scores }}</h3>
    <h3>{{ scores.0 }}</h3>
    <h3>{{ scores.1 }}</h3>
    <h3>{{ scores.2 }}</h3>

    {% for score in scores %}
        <h4>{{ score }}</h4>
    {% endfor%}
    <hr>
    <h3>{{ info.name }}</h3>
    <h3>{{ info.age }}</h3>

    {% for item in info.keys %}
        <h4>{{ item }}</h4>
    {% endfor%}

    {% for item in info.values %}
        <h4>{{ item }}</h4>
    {% endfor%}

    {% for key,value in info.items %}
        <h4>{{ key }}: {{value}}</h4>
    {% endfor%}
    <hr>

    {% if name == "Tom" %}
        <h3>The name is Tom</h3>
    {% else %}
        <h3>The name is not Tom</h3>
    {% endif %}
    

    <img src="{% static 'python.jpg' %}" alt="">
</body>
</html>
```



`view.py`

```
def computer_science(request):
    student = "Tom1"
    data = [80,90,100]
    info = {"name": "Jerry", "age":20, "score":90}
    return render(request, "cs.html", {"name":student, "scores":data, "info":info})

```



### request and response

```python
def request_response(request):

    ## request
    # GET/POST
    print(request.method)

    # http://127.0.0.1:8000/test/?name=Tom
    print(request.GET)

    # 
    print(request.POST)

    ## response
    # HttpResponse()
    # return a sting

    # render(request, "xx.html")
    # return a rendered html file

    # redirect("http://www.google.com")
    # redirection
    return redirect("http://www.google.com")
```

##### redirection

![redirection](data\redirection.jpg)



### example_login

![example](data\example.jpg)



`login.html`

```
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>

    <h1>login</h1>
    <form action="/login/" method="post">
    {% csrf_token%}
    <input type="text" name="user" >
    <input type="password" name="pwd" >
    <input type="submit" value="login"> 
    <span style="color: red;">{{ msg }}</span>
    
    </form>
</body>
</html>
```

### Cross Site Request Forgery (CSRF)

![csrf](data\csrf.jpg)





### Database

#### install mysql-connector-python

https://dev.mysql.com/doc/connector-python/en/connector-python-django-backend.html

#### ORM

- can not be used to create a database
- modify a table
- modify the data in tables

create a database in MySQL

```sql
create database mydatabase1 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

`setting.py`

```
DATABASES = {
    'default': {
        'NAME': 'mydatabase1',
        'ENGINE': 'mysql.connector.django',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '1234',
        'OPTIONS': {
          'autocommit': True,
          'use_oure': True,
          'init_command': "SET foo='bar';"
        },
    }
}
```

Sometimes `OPTIONS` is not required

`setting.py`


```
DATABASES = {
    'default': {
        'NAME': 'mydatabase1',
        'ENGINE': 'mysql.connector.django',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '1234',
    }
}
```





`app1/models.py`

```python
from django.db import models

# Create your models here.

# inherit from (models.Model
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()
    score = models.IntegerField(default=2)
    department = models.IntegerField(null=True, blank=True)


'''
same as the sql query

create table app1_userinfo(
    id bigint auto_increment primary key,
    name varchar(32),
    password varchar(32)
    age int
)
'''

```

#### database migration

#### create tables

```
python manage.py makemigrations
python manage.py migrate
```

can be used to add a new table

#### delete a field

- remove the corresponding attribute
- database migration

#### add a field

- add the corresponding attribute

- database migration

  - enter a default value

  - pass an argument `default`

  - allow NULL values




#### CRUD

```
def orm(request):
    # # create
    # UserInfo.objects.create(name="Tom", password="123", age = 20)
    # UserInfo.objects.create(name="Jerry", password="456", age = 26)
    # UserInfo.objects.create(name="Mike", password="789") # default value is 2

    # # delete
    # UserInfo.objects.filter(id=8).delete()

    # # read
    # res = UserInfo.objects.all()
    # print(res)
    # for item in res:
    #     print(item.name, item.password)

    # res = UserInfo.objects.filter(id=1)
    # item = res.first()
    # print(item.name, item.password)

    # # update
    # UserInfo.objects.filter(id=7).update(age=100)
    return HttpResponse("executed")
```



### example

#### display the information of users

![example](data\example1.jpg)



`user_list.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<table border="2">
    <thead>
        <tr>
            <th>id</th>
            <th>name</th>
            <th>pwd</th>
            <th>age</th>
        </tr>
    </thead>
    
    <tbody>
        {% for item in users %}
        <tr>
            <td>{{ item.id }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.password }}</td>
            <td>{{ item.age }}</td>
        </tr>
        {% endfor %}
    
    </tbody>
</table>

    
</body>
</html>
```

#### add users

![example](data\example2.jpg)



`user_add.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>

    <h1>add user</h1>
    <form action="/user/add/" method="post">
    
    {% csrf_token%}
    <input type="text" name="user" >
    <input type="text" name="password" >
    <input type="text" name="age" >
    <input type="submit" value = "add">
    
    
    </form>
</body>
</html>
```

add to  `user_list.html`

```html
    <a href="/user/add/">add user</a>
```



#### delete users

![example](data\example3.jpg)

```python
def user_delete(request):
    # receive data from the user
    uid = request.GET.get("uid")
    # delete from the database
    UserInfo.objects.filter(id=uid).delete()
    return HttpResponse("deleted")
    # return redirect("/user/list/")
```

http://127.0.0.1:8000/user/delete/?uid=7



#### delete users 2

modify `user_list.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <a href="/user/add/">add user</a>
<table border="2">
    <thead>
        <tr>
            <th>id</th>
            <th>name</th>
            <th>pwd</th>
            <th>age</th>
        </tr>
    </thead>
    
    <tbody>
        {% for item in users %}
        <tr>
            <td>{{ item.id }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.password }}</td>
            <td>{{ item.age }}</td>
            <td>
                <a href="/user/delete/?uid={{ item.id }}"> delete </a>
            </td>
        </tr>
        {% endfor %}
    
    </tbody>
</table>

    
</body>
</html>
```



### another example

#### register for the app

#### database

##### database configuration

`setting.py`


```
DATABASES = {
    'default': {
        'NAME': 'mydatabase1',
        'ENGINE': 'mysql.connector.django',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '1234',
    }
}
```

##### create a database in MySQL

```sql
create database mydatabase2 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

- user orm to create tables

```python
from django.db import models

# Create your models here.

# inherit from models.Model

class Department(models.Model):
    name = models.CharField(verbose_name="department name", max_length=32)

class Student(models.Model):
    name = models.CharField(verbose_name="student name", max_length=32)
    pwd = models.CharField(verbose_name="student pwd", max_length=32)
    age = models.IntegerField(verbose_name="student age")
    balance = models.DecimalField(verbose_name="student balance", max_digits=10, decimal_places=2, default=0)
    enrollment_date = models.DateField(verbose_name="student enrollment date")


    ## no constraint
    # d_id = models.BigIntegerField(verbose_name="student department id")

    ## to: table Department
    ## to_field: field id
    ## will generate a field 'Department' in the student table

    # department = models.ForeignKey(to="Department", to_field="id")
    # this will cause an error


    # delete a department in the Department table
    # cascade
    department = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)
    # # set null
    # department = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)

    # gender
    gender_identity = ((1,'male'),(2,'female'))
    gender = models.SmallIntegerField(verbose_name="student gender",choices=gender_identity)


```



![tables](data\tables.png)




Do we use the department name or department id in the Employee table?

- 
  id: less space complexity

- name: less time complexity




- The department_id must be in the Department table

- Deleting a department in the Department table:

  - cascade delete

  - set null

- create a field for the gender?

  - categorical data

##### generate tables

```
python manage.py makemigrations
python manage.py migrate
```



#### static files

#### url -function mapping

`mysite2/urls.py`

```python
from django.contrib import admin
from django.urls import path
from app01 import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dept/list/', views.dept_list),
]

```

`mysite2/app01/views.py`

```python
from django.shortcuts import render, HttpResponse

# Create your views here.
def department_list(request):
    # return HttpResponse("department_list") 
    return render(request, dept_list.html)
```

#### create a template

`dept_list.html`

![department](data\department.jpg)

#### add data to the table

```sql
insert into mydatabase2.app01_department(name) values("CS"),("Math");
```



#### dept_list

`mysite2/app01/views.py`

```python
def dept_list(request):
    # return HttpResponse("department_list") 

    res = models.Department.objects.all()
    return render(request, 'dept_list.html', {'depts':res})
```

##### result

![department](data\department2.jpg)

#### dept_add

`mysite2/app01/views.py`

```python
def dept_add(request):
    if request.method == "GET":
        return render(request, 'dept_add.html')

    dept_name = request.POST.get("dept_name")

    # add to database
    models.Department.objects.create(name=dept_name)

    return redirect("/dept/list/")   
```

##### result

![department](data\department3.jpg)

#### dept_del

`mysite2/app01/views.py`

```
def dept_del(request):

    dept_id = request.GET.get("dept_id")

    # update database
    models.Department.objects.filter(id=dept_id).delete()

    return redirect("/dept/list/")   
```

`dept_list.html`

```html
<a class="btn btn-danger btn-sm" href="/dept/del/?dept_id={{ dept.id }}" role="button">delete</a>
```

#### dept_edit

`mysite2/app01/views.py`

```python
def dept_edit(request,dept_id):
    return render(request, 'dept_edit.html')
```

`dept_list.html`

```html
<a class="btn btn-secondary btn-sm" href="/dept/{{ dept.id }}/edit/" role="button">edit</a>
```

##### change the default value

`mysite2/app01/views.py`

```python
def dept_edit(request,dept_id):
    res = models.Department.objects.filter(id=dept_id).first()
    print(res)
    print(res.id,res.name)
    return render(request, 'dept_edit.html',{'res':res})
```

`dept_edit.html`

```html
<input class="form-control" type="text" placeholder="{{ res.name }}" name="dept_name">
```



![department](data\department4.jpg)

##### submit

`mysite2/app01/views.py`

```python
def dept_edit(request,dept_id):
    if request.method == "GET":
        res = models.Department.objects.filter(id=dept_id).first()
        # print(res)
        # print(res.id,res.name)
        return render(request, 'dept_edit.html',{'res':res})

    new_dept_name = request.POST.get("new_dept_name")
    models.Department.objects.filter(id=dept_id).update(name = new_dept_name)
    return redirect("/dept/list/") 
```

`dept_edit.html`

```html
<input class="form-control" type="text" placeholder="{{ res.name }}" name="new_dept_name">
```



### template inheritance

some html files share the same components

`layout.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <nav class="navbar navbar-expand-lg bg-light">
            <div class="container-fluid">
              <a class="navbar-brand" href="#">MySAU</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Department</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                  </li>



                  <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Tom
                    </a>
                    <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="#">user info</a></li>
                      <li><a class="dropdown-item" href="#">account setting</a></li>
                      <li><hr class="dropdown-divider"></li>
                      <li><a class="dropdown-item" href="#">logout</a></li>
                    </ul>
                  </li>
                </ul>



              </div>

              
            </div>
          </nav>
    </div>

    {% block content %}
    {% endblock%}


</body>
</html>
```

`index.html`

```html
{% extends 'layout.html'%}

{% block block1 %}
    <h1>Hello SAU</h1>

{% endblock%}
```

### User

```sql
insert into app01_student(name, pwd, age, balance, enrollment_date, gender, department_id) values("Tom", 123, 20, 1000, "2022-11-1", 1, 1)

insert into app01_student(name, pwd, age, balance, enrollment_date, gender, department_id) values("Jerry", 456, 25, 1500, "2021-08-1", 1, 2)

insert into app01_student(name, pwd, age, balance, enrollment_date, gender, department_id) values("Jane", 789, 30, 2000, "2020-12-1", 2, 1)
```

`stu_list.html`



#### add user

`stu_add.html`





#### ModelForm

`stu_add_modelform.html`

```html
		<div class="card-body">
            <form method="post">    
                {% csrf_token %}
                {% for field in form %}
                    {{ field.label }}: {{ field }}
                {% endfor %}

                <button type="submit" class="btn btn-primary">Submit</button>
              </form>
        </div>
```

`mysite2/app01/views.py`

```python
from django import forms
class StuModelForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ["name","pwd","age","balance","enrollment_date","gender","department"]

def stu_add_modelform(request):
    form = StuModelForm()
    return render(request, "stu_add_modelform.html", {"form":form})
```

