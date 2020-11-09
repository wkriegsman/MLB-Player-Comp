from django.urls import path
from . import views

from .views import get_data, ChartData

urlpatterns = [
    path('', views.home, name='home'),
    path('players/', views.players, name='players'),
    path('players/<int:player_id>/', views.player_detail, name='detail'),
    path('players/<int:player_id>/delete/', views.player_delete, name='player_delete'),
    path('players/<int:player_id>/edit/', views.player_edit, name='player_edit'),
    path('batters/', views.batters, name='batters'),
    # path('batters/', views.BattersResultsView.as_view(), name='batters'),
    path('pitchers/', views.pitchers, name='pitchers'),
    path('api/data/', get_data, name='api-data'),
    path('api/chart/data/', ChartData.as_view()),
]