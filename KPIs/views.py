from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.


def welcome(request):
    areas = Area.objects.all()
    indicators = Indicators.objects.all()
    print(indicators)
    return render (request, 'home.html',{"areas":areas,"indicators":indicators})  

@login_required
def score(request):
    current_user = request.user 
    return render (request, 'score.html')


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
        
