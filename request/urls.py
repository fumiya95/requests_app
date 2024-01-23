from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path
app_name = "request"
urlpatterns = [
  path('', views.index, name='index'),
 
]