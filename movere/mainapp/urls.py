from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('home/', views.home, name='home'),
    path('make_order/', views.make_order, name='make_order'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('storage/', views.storage, name='storage'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
]
