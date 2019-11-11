from django.shortcuts import render

# Create your views here.
def kpis(request):
    return render(request, 'kpis.html', {"kpis":kpis})