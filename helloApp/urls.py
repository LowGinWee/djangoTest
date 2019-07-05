from helloApp import views
from django.urls import path
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_url>/', views.category, name='category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_url>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='login')

    ]
