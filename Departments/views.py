from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.template.loader import render_to_string
from users.models import UserProfile
from Departments.models import *
from Departments.forms import *
# test


# Create your views here.
@login_required(login_url='/users/')
def add_department_view(request):
    form = DepartmentCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = DepartmentCreationForm()

    return render(request, 'add_department.html', {"form": form})


@login_required(login_url='/users/')
def list_departments_view(request):
    departments = Department.get_all_departments()
    context = {'departments': departments}
    return render(request, 'departments_list.html', context)


@login_required(login_url="/users/")
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET['search']
        department = Department.objects.filter(
            name__icontains=search_term).first()
        department_users = UserProfile.objects.filter(
            department=department).all()
        context = {
            "department_users": department_users
        }
        return render(request, 'departments.html', context)
    return render(request, 'departments.html')


# correct
def department_list_view(request):
    departments = Department.get_all_departments()
    context = {'departments': departments}
    return render(request, 'department_list.html', context)


def department_create_view(request):
    data = dict()

    if request.method == 'POST':
        form = DepartmentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            departments = Department.objects.all()
            data['html_dept_list'] = render_to_string(
                'partial_department_list.html', {'departments': departments})
        else:
            data['form_is_valid'] = False
    else:
        form = DepartmentCreationForm()

    context = {'form': form}
    data['html_form'] = render_to_string(
        'partial_department_create.html', context, request=request,)
    return JsonResponse(data)
