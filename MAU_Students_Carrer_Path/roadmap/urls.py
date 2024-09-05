# urls.py
from django.urls import path
from . import views
from .views import restricted

urlpatterns = [
    path('', views.index, name='index'),
     path('restricted/', restricted, name='restricted'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('roadmap/<int:roadmap_id>/', views.roadmap_detail, name='roadmap_detail'),
]
