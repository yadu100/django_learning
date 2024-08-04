from django.shortcuts import render, redirect
from .models import EmployeeDatabase, EmployeeReview, SkillSet

from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import EmployeeForm, CustomUserCreationForm

from .utils import SerachItem, Paginate

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


####### ----------------- Password reset imports  --------------------##############
from django.contrib.auth.forms import PasswordChangeForm


EmployeeDatabaseItem = EmployeeDatabase.objects.all()
@login_required
def changePassword(request):
    form = PasswordChangeForm(request.user)
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            login(request,request.user)
            return redirect('Home')

    return render(request, 'EmployeeDbase/password_Reset.html',{'form':form})


def callHomePage(request):

    EmployeeDatabaseItem, search_query = SerachItem(request)

    EmployeeDatabaseItem, custom_range, paginator = Paginate(request, EmployeeDatabaseItem)

    return render(request, 'EmployeeDbase/Homepage.html',
                  {'employee_datas':EmployeeDatabaseItem, 'search_query':search_query, 'paginator':paginator, 'custom_range':custom_range})



def callSingleEmployeePage(request,emp_name):
    search_employee = EmployeeDatabase.objects.get(name=emp_name)
    return render(request, 'EmployeeDbase/IndividualEmployee.html', {'employee_data':search_employee})


@login_required(login_url="login")
def callEmployeeAdditionPage(request):

    employeeform = EmployeeForm()

    #adding functionality
    if request.method=='POST':
        employeeform = EmployeeForm(request.POST, request.FILES)
        if employeeform.is_valid():
            employeeform.save()
            return redirect('Home')
    return render(request, 'EmployeeDbase/Employee_Addition_form.html',{'form':employeeform})

@login_required(login_url="login")
def callEmployeeUpdateForm(request,name):
    employee = EmployeeDatabase.objects.get(name=name)
    employeeform = EmployeeForm(instance=employee)
    if request.method=='POST':
        employeeform = EmployeeForm(request.POST, request.FILES,instance=employee)
        employeeform.save()
        return redirect('Home')
    return render(request, 'EmployeeDbase/Employee_update_form.html', {'form':employeeform})

@login_required(login_url="login")
def callEmployeeDeleteForm(request,name):
    employee = EmployeeDatabase.objects.get(name=name)
    name =  employee.name
    if request.method == 'POST':
        employee.delete()
        return redirect('Home')
    return render(request, 'EmployeeDbase/Employee_delete_form.html', {'employee':name})



def loginUser(request):

    page = "login"

    if request.user.is_authenticated:
        return redirect('Home')

    if request.method == 'POST':
        #print(request.POST)
        user_name = request.POST['Username']
        password = request.POST['Password']
        #print(user_name)
        #print(password)

        #checking whether the username is present in user database model 
        
        try:
            user = User.objects.get( username = user_name )
        except:
            messages.error(request,"User name doesnot exist")
            

        user = authenticate(request, username = user_name, password = password)
        #print(user)

        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request,"incorrect user name or password")



    return render(request, 'EmployeeDbase/login.html',{'page':page})


def logoutUser(request):
    logout(request)
    return redirect('Home')

def registerUser(request):
    page = "register"
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"User Registered Successfully")
            return redirect('Home')
        else:
            messages.error(request,"There was a problem registering User. Please try again")

    return render(request, 'EmployeeDbase/login.html',{'page':page,'form':form})


