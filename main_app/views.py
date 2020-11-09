from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView
from .models import Batters, Pitchers

# Create your views here.
def home(request):
    return render(request, 'home.html')

def batters(request):
    return render(request, 'batters.html')

# class BattersResultsView(ListView):
#     model = Batters
#     template_name = 'batters.html'

def pitchers(request):
    return render(request, 'pitchers.html')   


def get_data(request, *args, **kwargs):
    data = {
    "ab": 470,
    "avg": .291,
    "babip": .298,
    "h": 137,
    "hr": 45,
    "obp": .438,
    "ops": 1.083,
    "r": 110,
    "rbi": 104,
    "sb": 11,
    "slg": .645,
    "so": 11,
    "vorp": 81.5,
    "warp": 9.34,
    }
    return JsonResponse(data)


class ChartData(APIView):
    
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "ab": 470,
            "avg": .291,
            "babip": .298,
            "h": 137,
            "hr": 45,
            "obp": .438,
            "ops": 1.083,
            "r": 110,
            "rbi": 104,
            "sb": 11,
            "slg": .645,
            "so": 11,
            "vorp": 81.5,
            "warp": 9.34,
    }
        return Response(data)

        