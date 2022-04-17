from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import EmployeeRegistration
from .models import Employee
from django.contrib import messages

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
            """Using Form you can just check form is valid or not
            and if it's valid then you can use save() function to
            save all fields"""
            # fm.save()
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            salary = fm.cleaned_data['salary']
            emp = Employee(name=name, email=email, salary=salary)
            emp.save()
            fm = EmployeeRegistration()
            messages.success(request,"Data inserted Successfully..!")
    else:
        fm = EmployeeRegistration()
    emp = Employee.objects.all()

    return render(request, 'enroll/addandshow.html', {'form':fm, "emp": emp})

def update_data(request, id):
    emp = Employee.objects.get(pk=id)
    if request.method == "POST":
        emp_form = EmployeeRegistration(request.POST, instance=emp)
        if emp_form.is_valid():
            emp_form.save()
            messages.success(request,"Data updated  Successfully..!")
        else:
        	messages.warning(request,"Sorry, Form data is not valid..!")
    else:
        emp_form = EmployeeRegistration(instance=emp)
    return render(request, 'enroll/update_employee.html', {'form':emp_form})

def delete_data(request, id):
    if request.method == "POST":
        emp = Employee.objects.get(pk=id)
        emp.delete()
        messages.error(request,"Data deleted Successfully..!")
    return redirect(add_show) 

