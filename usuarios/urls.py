from django.urls import path
from vistaprevia import views
from vistaprevia import views_login
from vistaprevia import views_logout
from vistaprevia import views_registro

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.index, name='id'),
    path('', views.index, name='index'),
    path('', views.index, name='index'),
]