from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from Departments.models import Department
from Departments.forms import DepartmentCreationForm


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


@login_required(login_url='/users/')
def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request, 'book/upload_form.html', {'upload_form': book_form})


@login_required(login_url='/users/')
def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')
