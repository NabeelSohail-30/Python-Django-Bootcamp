from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home2/', views.view_home_page, name='view_home_page'),
]
