"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,include

from app1 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),
    path('user/', views.user),
    path('cs/index', views.computer_science),
    path('app1/', include('app1.urls')),
    path('test/', views.request_response),
    path('login/', views.login),
    path('orm/', views.orm),
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/delete/', views.user_delete),


    path('example2/', views.example2),
]
