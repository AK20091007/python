from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from app import views

urlpatterns = [
    path('course/list/', views.course_list),
    path('course/<int:number>/add/', views.add),
    path('course/<int:number>/drop/', views.drop),
    path('course/<int:number>/delete/', views.delete),
    path('course/add/', views.add_course),
]
