from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from KPIs.forms import *
from KPIs.models import *

# Create your views here.


def kpis(request):
    return render(request, 'kpis.html', {"kpis": kpis})


def graphs(request):
    return render(request, 'reports.html', {"reports": reports})


@login_required(login_url='users/')
def area(request):

    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        form = AddArea(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.save()

        return redirect('/')

    else:

        form = AddArea()

    return render(request, 'new_area.html', {"form": form})
