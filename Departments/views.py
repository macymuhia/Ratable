from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from .models import Department,Staff
from .forms import DepartmentCreationForm,EditDepartmentForm
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
@login_required(login_url='account/login/')
def index(request):
    name = 'departments'
    if request.method == 'POST':
        form = departmentCreationForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.user = current_user
            department.save()
            return redirect('home')
        else:
           form = DepartmentCreationForm()
        return render(request,
                      'departments.html', 
                      {"user":current_user,
                        "comment_form":form}
                )
   
def edit_deparments(request, department):
    department = Department.objects.get(department=department)
    
    if request.method == 'POST':
        
        form = EditDepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            update = form.save(commit=False)

            form.save()
            return redirect('profile')
    else:
        form = EditDeparmentForm()
    return render(request, 'edit_department.html', {'form': form})
    
def searchresult(request):
    if request.method == "GET":
        search = request.GET.get('user__username=request.user.username')
        departments = Department.objects.filter(department_name=search)
        users = User.objects.filter(user__username__icontains=search)
        
    return render(request, 'user/searchresult.html', {"departments":departments, "users":users})

