from django.shortcuts import render, redirect

from employee.models import Employee

from employee.forms import EmployeeForm

def index(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'employee/index.html', context)

def add(request):
    employees = Employee.objects.all()
    form = EmployeeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    
    context = {
        'form': form,
        'employees': employees,
    }
    return render(request, 'employee/add.html', context)

def updateEmployee(request, pk):
    employee = Employee.objects.get(pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('index')
    
    context = {
        'form': form,
        'employee': employee,
    }
    return render(request, 'employee/edit_employee.html', context)

def deleteEmployee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('index')