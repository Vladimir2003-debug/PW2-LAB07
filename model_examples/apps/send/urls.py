from django.contrib import admin
from django.urls import path
from .views import index,index_view

urlpatterns = [
    path('send/', index),    
    path('', index_view ,name='index')    

]
