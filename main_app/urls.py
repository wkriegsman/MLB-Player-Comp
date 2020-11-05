from django.urls import path
from . import views

from .views import get_data, ChartData

urlpatterns = [
    path('', views.home, name='home'),
    path('batters/', views.batters, name='batters'),
    path('pitchers/', views.pitchers, name='pitchers'),
    path('api/data/', get_data, name='api-data'),
    path('api/chart/data/', ChartData.as_view()),
]