from django.urls import path
from src import views

urlpatterns = [
    path('', views.home, name='index'),
    path('calc/', views.cal, name='calc'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('contact', views.contact, name='contact')
]
