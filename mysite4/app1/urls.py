from django.urls import path
from app1 import views

urlpatterns = [
    path('list/', views.mysite4List),
    path('<int:course_id>/add/', views.add_student),
    path('<int:course_id>/drop/', views.drop_student),
    path('<int:course_id>/delete/', views.delete_student),
    path('add/', views.add_studentForm),
]
