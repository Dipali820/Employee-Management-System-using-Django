from django.shortcuts import render,redirect
from .models import EmpModel
from django.contrib import messages


# Create your views here.
def index_view(request):
     return render(request,'index.html')
    
def Empmodel_view(request):
    if request.method=="GET" and 'empid' in request.GET:
        empid=request.GET.get('empid')
        name=request.GET.get('name')
        department=request.GET.get('department')
        salary=request.GET.get('salary')
       
        EmpModel.objects.create(empid=empid , name=name, department=department,salary=salary)
        messages.success(request, f"Employee {name} Created successfully!")
        
        return redirect('showemployee') #for direct redirect the list page
    return  render(request,'addemployee.html')

def update_employee(request):
    if request.method == 'POST':
        empid = request.POST.get('empid')
        salary = request.POST.get('salary')
        department = request.POST.get('department')

        print("empid =", empid)
        print("salary =", salary)
        print("department =", department)

        result = EmpModel.objects.filter(empid=empid).update(salary=salary, department=department)

        if result:
            messages.success(request, f"Employee {empid} updated successfully! Dept: {department}, Salary: {salary}")
        else:
            messages.error(request, f"No employee found with empid = {empid}.")
            
        return redirect('showemployee')

    return render(request, 'updateemployee.html')


def delete_employee(request):
    if request.method=="GET" and 'empid' in request.GET:
        empid=request.GET.get('empid')
        name=request.GET.get('name')
        
        k=EmpModel.objects.filter(empid=empid,name=name).delete()
        messages.success(request, f"Employee {name} Deleted successfully!")
        
        return redirect('showemployee')
        
    return render(request,'deleteemployee.html')


def show_employee(request):
     employees = EmpModel.objects.all()
     return render(request, 'showemployee.html', {'employees': employees})