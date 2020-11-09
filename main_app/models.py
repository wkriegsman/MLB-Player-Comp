from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=40)
    team = models.CharField(max_length=50)

class Homeruns(models.Model):
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    hr2020 = models.IntegerField()
    hr162 = models.IntegerField()


class Batters(models.Model):
    name = models.CharField(max_length=40)
    ab = models.IntegerField()
    avg = models.DecimalField(max_digits=4, decimal_places=3)
    babip = models.DecimalField(max_digits=4, decimal_places=3)
    h = models.IntegerField()
    hr = models.IntegerField()
    obp = models.DecimalField(max_digits=4, decimal_places=3)
    ops = models.DecimalField(max_digits=4, decimal_places=3)
    r = models.IntegerField()
    rbi = models.IntegerField()
    sb = models.IntegerField()
    slg = models.DecimalField(max_digits=4, decimal_places=3)
    so = models.IntegerField()
    vorp = models.DecimalField(max_digits=4, decimal_places=1)
    warp = models.DecimalField(max_digits=4, decimal_places=2)

class Pitchers(models.Model): 
      name = models.CharField(max_length=40)
      dra = models.DecimalField(max_digits=4, decimal_places=2)
      era = models.DecimalField(max_digits=4, decimal_places=2)
      hr9 = models.DecimalField(max_digits=4, decimal_places=2)
      ip = models.DecimalField(max_digits=4, decimal_places=1)
      so = models.IntegerField()
      so9 = models.DecimalField(max_digits=4, decimal_places=1)
      sv = models.IntegerField()
      vorp = models.DecimalField(max_digits=4, decimal_places=1)
      warp = models.DecimalField(max_digits=4, decimal_places=2)
      whip = models.DecimalField(max_digits=4, decimal_places=2)
