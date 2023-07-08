from django.contrib import admin
from .views import GeneratePdf
from django.urls import path

urlpatterns = [
    path('',GeneratePdf.as_view(), name="pdf"),
]
