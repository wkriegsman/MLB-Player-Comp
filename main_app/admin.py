from django.contrib import admin
from .models import Batters, Pitchers, Player, Homeruns

# Register your models here.

admin.site.register(Batters)
admin.site.register(Pitchers)
admin.site.register(Player)
admin.site.register(Homeruns)
