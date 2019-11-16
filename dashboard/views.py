from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return redirect('dashboard')


@login_required(login_url='users/')
def dashboard(request):
    return render(request, 'dashboard.html')
