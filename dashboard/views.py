from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return redirect('landing_page')


@login_required(login_url='users/')
def landing_page_view(request):
    return render(request, 'landing_page.html')


@login_required(login_url='users/')
def dashboard_view(request):
    return render(request, 'dashboard.html')
