from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def batters(request):
    return render(request, 'batters.html')

def pitchers(request):
    return render(request, 'pitchers.html')    