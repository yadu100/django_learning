from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.callHomePage, name="Home"),
    path('Employee/<str:emp_name>', views.callSingleEmployeePage, name="Employee"),
    path('add-employee/',views.callEmployeeAdditionPage,name="add-employee"),
    path('update-employee/<str:name>', views.callEmployeeUpdateForm, name="update-employee"),
    path('delete-employee/<str:name>',views.callEmployeeDeleteForm, name='delete-employee'),


    
]