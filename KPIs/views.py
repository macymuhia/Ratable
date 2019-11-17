
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
def kpis(request):
    return render(request, 'kpis.html', {"kpis": kpis})

def welcome(request):
    areas = Area.objects.all()
    indicators = Indicators.objects.all()
    print(indicators)
    return render (request, 'home.html',{"areas":areas,"indicators":indicators})  


@login_required
def score(request):
    current_user = request.user 
    return render (request, 'score.html')


def reports(request):
    return render(request, 'reports.html', {"reports":reports})

def comments(request):
    return render(request, 'comments.html')

def new_area(request):
    
    if request.method == 'POST':

        form = AddArea(request.POST)

        if form.is_valid():
            
            post = form.save(commit = False)
            post.save()

        return redirect('/')

    else:

        form = AddArea()
        
    return render(request,'addarea.html',{"form":form}) 


def areas(request):
    areas = Area.objects.all()
    return render(request,'home.html',{"areas":areas}) 


def new_indicator(request):
    
    if request.method == 'POST':
        
        form = AddIndicator(request.POST)
        
        if form.is_valid():
            
            post = form.save(commit = False)
            post.save()
            
        return redirect('/')
    
    else:
        
        form = AddIndicator()
        
    return render(request,'addindicator.html',{"form":form})

def new_score(request):
    if request.method == 'POST':

        score = request.POST.get('options')
        ind = request.POST.get('indicator')

        Score(
            score=score,
            indicators_id=ind,
            user=request.user
        ).save()

        return redirect('/')

    return render(request, 'score.html')

# View fucntion for our rating metric that will be logic for the rating.
@login_required
def rateproject(request, id):

    if request.method == "POST":
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            area_total = []
            area_max_total = []
            areas = Area.objects.get(pk=id)
            indicators = Indicators.objects.filter(area=areas)
            area_total.append(indicators)
            area_average = sum(area_total)/len(area_total)
            print(area_average)
            area_max_total.append(area_average)
            area_max_total_average= sum(area_max_total)/len(area_max_total)
            print(area_max_total_average)
            reports = Reports(area_average=area_average,overall_score=area_max_total_average)
            reports.user = request.user
            reports.project = Departments.objects.filter(id=id).first()
            reports.save()
            return redirect('/')
    else:
        rating_form = RatingForm()

    return render (request, 'reports.html', {"area_average":area_average, "area_max_total_average":area_max_total_average })