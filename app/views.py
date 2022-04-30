from django.shortcuts import redirect, render
from app.models import Employee

def index(request):
    emp = Employee.objects.all()
    return render(request,"index.html",{'employee':emp})

def create(request):
    if request.method =="POST" :
        name = request.POST["name"]
        address = request.POST["address"]
        designation = request.POST["designation"]
        salary =request.POST["salary"]
        emp = Employee(name=name,address=address,designation=designation,salary=salary)
        emp.save()
        return redirect('home')
    return render(request,"create.html")
    
def delete(request,id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('home')


def update(request,id):
    emp = Employee.objects.get(id=id)
    if request.method == "POST":
        emp.name = request.POST["name"]
        emp.address = request.POST["address"]
        emp.designation = request.POST["designation"]
        emp.salary = request.POST["salary"]
        emp.save()
        return redirect('/')
    return render(request,'update.html',{'employee':emp})


