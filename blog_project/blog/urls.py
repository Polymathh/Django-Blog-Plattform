from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #Custom views for your blog
    path('', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('post_list', views.post_list, name='post_list'),

    #authentication views using Django built in views
    
    path('logout', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register', views.register, name='register'),
    path('post/create/', views.post_create, name='post_create'), 
]