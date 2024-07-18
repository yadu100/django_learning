from django.contrib import admin
from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.callHomePage, name="Home"),
    path('Employee/<str:emp_name>', views.callSingleEmployeePage, name="Employee"),
    path('add-employee/',views.callEmployeeAdditionPage,name="add-employee"),
    path('update-employee/<str:name>', views.callEmployeeUpdateForm, name="update-employee"),
    path('delete-employee/<str:name>',views.callEmployeeDeleteForm, name='delete-employee'),


    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)