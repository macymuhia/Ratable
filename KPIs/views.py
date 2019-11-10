from django.shortcuts import render
from forms import *
from models import *

# Create your views here.

@login_required(login_url='/accounts/login')
def area(request):

    profile = Profile.objects.get(user = request.user)
    
    if request.method == 'POST':
        
        form = AddArea(request.POST)
        
        if form.is_valid():
            
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            
        return redirect('/')
    
    else:
        
        form = AddArea()
        
    return render(request, 'new_area.html', {"form": form})    