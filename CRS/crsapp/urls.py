from django.urls import path
from crsapp import views

urlpatterns = [
    path('list/', views.courseMenu),
    path('<int:course_number>/add/', views.addID),
    path('<int:course_number>/drop/', views.dropID),
    path('<int:course_number>/delete/', views.deleteCRS),
    path('add/', views.addForm),
]
