from django.urls import path
from app import views

urlpatterns = [
    path('list/', views.class_main),
    path('<int:id>/add/', views.add_class),
    path('<int:id>/drop/', views.drop_class),
    path('<int:id>/delete/', views.delete_class),
    path('add/', views.add_classForm),
]
