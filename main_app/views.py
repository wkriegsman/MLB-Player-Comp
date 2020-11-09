from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView
from .models import Batters, Pitchers, Player, Homeruns
from .forms import Player_Form

# Create your views here.
def home(request):
    return render(request, 'home.html')

# index page
def players(request):
    if request.method == 'POST':
        player_form = Player_Form(request.POST)
        if player.form.is_valid():
            player_form.save()
            return redirect('players')
    players = Player.objects.all()
    print(players)
    player_form = Player_Form()
    context = {'players': players, 'player_form': player_form}
    return render(request, 'players.html', context)  

# show page
def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    context = {'player': player}
    return render(request, 'players/detail.html', context) 
         
# edit and update
def player_edit(request, player_id):
  player = Player.objects.get(id=player_id)
  if request.method == 'POST':
    player_form = Player_Form(request.POST, instance=player)
    if player_form.is_valid():
      player_form.save()
      return redirect('detail', player_id=player_id)
  else:  
    player_form = Player_Form(instance=player)
  context = {'player': player, 'player_form': player_form}
  return render(request, 'player/edit.html', context)

# delete
def player_delete(request, player_id):
    Player.objects.get(id=player_id).delete()
    return redirect("players")

    
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

        