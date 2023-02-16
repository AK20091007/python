from django.urls import path
from django.conf.urls import include
from app import views

urlpatterns = [
    path('course/', include('app.urls')),
]
