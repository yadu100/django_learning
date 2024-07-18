from django.shortcuts import render, redirect
from .models import EmployeeDatabase, EmployeeReview, SkillSet

from .forms import EmployeeForm

EmployeeDatabaseItem = EmployeeDatabase.objects.all()


def callHomePage(request):
    return render(request, 'EmployeeDbase/Homepage.html',{'employee_datas':EmployeeDatabaseItem})

def callSingleEmployeePage(request,emp_name):
    search_employee = EmployeeDatabase.objects.get(name=emp_name)
    return render(request, 'EmployeeDbase/IndividualEmployee.html', {'employee_data':search_employee})

def callEmployeeAdditionPage(request):

    employeeform = EmployeeForm()

    #adding functionality
    if request.method=='POST':
        employeeform = EmployeeForm(request.POST)
        if employeeform.is_valid():
            employeeform.save()
            return redirect('Home')
    return render(request, 'EmployeeDbase/Employee_Addition_form.html',{'form':employeeform})


def callEmployeeUpdateForm(request,name):
    employee = EmployeeDatabase.objects.get(name=name)
    employeeform = EmployeeForm(instance=employee)
    if request.method=='POST':
        employeeform = EmployeeForm(request.POST,instance=employee)
        employeeform.save()
        return redirect('Home')
    return render(request, 'EmployeeDbase/Employee_update_form.html', {'form':employeeform})

def callEmployeeDeleteForm(request,name):
    employee = EmployeeDatabase.objects.get(name=name)
    name =  employee.name
    if request.method == 'POST':
        employee.delete()
        return redirect('Home')
    return render(request, 'EmployeeDbase/Employee_delete_form.html', {'employee':name})
