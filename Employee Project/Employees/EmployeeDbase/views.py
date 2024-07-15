from django.shortcuts import render
from .models import EmployeeDatabase, EmployeeReview, SkillSet

EmployeeDatabaseItem = EmployeeDatabase.objects.all()


def callHomePage(request):
    return render(request, 'EmployeeDbase/Homepage.html',{'employee_datas':EmployeeDatabaseItem})

def callSingleEmployeePage(request,emp_name):
    search_employee = EmployeeDatabase.objects.get(name=emp_name)
    return render(request, 'EmployeeDbase/IndividualEmployee.html', {'employee_data':search_employee})
