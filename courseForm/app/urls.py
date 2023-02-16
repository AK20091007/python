from django.urls import path
from app import views

urlpatterns = [
    path('list/', views.course_list),
    path('<int:formid>/add/', views.add_Course),
    path('<int:formid>/drop/', views.drop_Course),
    path('<int:formid>/delete/', views.delete_Course),
    path('add/', views.add_courseForm),
]
