from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.callHomePage, name="Home"),
    path('Employee/<str:emp_name>', views.callSingleEmployeePage, name="Employee")
    
]