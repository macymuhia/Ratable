from django.shortcuts import render

# Create your views here.
def Homeview(view):
    return render(request, 'dashboard.html', {"dashboard":dashboard})