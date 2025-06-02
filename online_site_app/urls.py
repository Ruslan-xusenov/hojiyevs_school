from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .views import logout_view, register_view

urlpatterns = [
    path('', views.news_list, name='home'),
    path('register/', register_view, name='register'),
    path('news/', views.news_list, name='news_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('location/', views.location, name='location'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
]