from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='todo/logout.html'), name='logout'),
    path('', views.task_list, name='task_list'),
    path('task/<int:task_id>/complete/', views.task_complete, name='task_complete'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
]