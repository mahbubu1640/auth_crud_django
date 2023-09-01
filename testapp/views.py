from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.

def home_page_view(request):
    return render(request,"testapp/home.html")

def logout_view(request):
    return render(request,"testapp/logout.html")

def sign_up_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})


from django.shortcuts import redirect
from .forms import EmployeeForm

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to a page showing employee list
    else:
        form = EmployeeForm()
    return render(request, 'testapp/employee_form.html', {'form': form})

from django.shortcuts import get_object_or_404
from .models import Employee

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'testapp/employee_list.html', {'employees': employees})

@login_required
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'testapp/employee_detail.html', {'employee': employee})


def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', id=id)  # Redirect to employee detail page
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'testapp/update_employee.html', {'form': form, 'employee': employee})


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')  # Redirect to employee list after deletion
    
    return render(request, 'testapp/delete_employee.html', {'employee': employee})
