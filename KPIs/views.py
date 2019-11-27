from django.db.models import Avg
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.


@login_required(login_url="/users/")
def kpis(request):
    return render(request, 'kpis.html', {"kpis": kpis})


@login_required(login_url="/users/")
def welcome(request):
    areas = Area.objects.all()
    indicators = Indicators.objects.all()
    print(indicators)
    return render(request, 'home.html', {"areas": areas, "indicators": indicators})


@login_required(login_url="/users/")
@login_required
def score(request):
    current_user = request.user
    return render(request, 'score.html')


@login_required(login_url="/users/")
def reports(request):
    return render(request, 'reports.html', {"reports": reports})


@login_required(login_url="/users/")
def comments(request):
    return render(request, 'comments.html')


@login_required(login_url="/users/")
def new_area(request):

    if request.method == 'POST':

        form = AddArea(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.save()

        return redirect('areas')

    else:

        form = AddArea()

    return render(request, 'addarea.html', {"form": form})


@login_required(login_url="/users/")
def areas(request):
    areas = Area.objects.all()
    return render(request, 'home.html', {"areas": areas})


@login_required(login_url="/users/")
def new_indicator(request):

    if request.method == 'POST':

        form = AddIndicator(request.POST)

        if form.is_valid():

            post = form.save(commit=False)

            post.save()

            form = AddIndicator()

    else:

        form = AddIndicator()

    return render(request, 'addindicator.html', {"form": form})


@login_required(login_url="/users/")
def new_score(request):
    if request.method == 'POST':

        score = request.POST.get('options')
        ind = request.POST.get('indicator')
        print(score)
        Score(
            score=score,
            indicators_id=ind,
            user=request.user
        ).save()

        return redirect('/kpis/')

    return render(request, 'score.html')

# View function for our rating metric that will be logic for the rating.


@login_required(login_url="/users/")
def score_reports(request):
    area = Area.objects.all()
    scores = Score.objects.filter(user=request.user).all()
    department = Department.objects.all()
    user_total = []
    user_area_total = []
    users = User.objects.all()

    for i in scores:
        user_total.append(i.score)
    user_average = sum(user_total)/len(user_total)
    return render(request, 'reports.html', {"scores": scores, "department": department, "users": users, "user_average": user_average})


@login_required(login_url="/users/")
def area_report(request):
    area = Area.objects.all()
    indicator = Indicators.objects.all()
    scores = Score.objects.all()
    averages = Score.objects.values(
        'indicators__area__name').annotate(average=Avg('score'))
    print(averages)

    return render(request, 'base-test.html', {"averages": averages})
