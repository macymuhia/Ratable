from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from Departments.models import Department
from Departments.forms import DepartmentCreationForm


# Create your views here.
def list_departments_view(request):
    departments = Department.get_all_departments()
    context = {'departments': departments}
    return render(request, 'departments.html', context)


@login_required(login_url='users/')
def add_department_view(request):
    form = DepartmentCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = DepartmentCreationForm()

    return render(request, 'add_department.html', {"form": form})
