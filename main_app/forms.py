from django.forms import ModelForm
from .models import Player


class Player_Form(ModelForm):
    class Meta:
        model = Player 
        fields = ['name', 'team']

        