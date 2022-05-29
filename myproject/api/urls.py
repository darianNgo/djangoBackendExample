from getpass import getuser
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    # path('users/', views.getUsers)
]
