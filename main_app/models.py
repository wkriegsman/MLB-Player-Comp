from django.db import models

# Create your models here.

class Batters(models.Model):
    name = models.CharField(max_length=40)
    ab = models.IntegerField()
    avg = models.DecimalField(decimal_places=3)
    babip = models.DecimalField(decimal_places=3)
    h = models.IntegerField()
    hr = models.IntegerField()
    obp = models.DecimalField(decimal_places=3)
    ops = models.DecimalField(decimal_places=3)
    r = models.IntegerField()
    rbi = models.IntegerField()
    sb = models.IntegerField()
    slg = models.DecimalField(decimal_places=3)
    so = models.IntegerField()
    vorp = models.DecimalField(decimal_places=1)
    warp = models.DecimalField(decimal_places=2)

class Pitchers(models.Model): 
      name = models.CharField(max_length=40)
      dra = models.DecimalField(decimal_places=2)
      era = models.DecimalField(decimal_places=2)
      hr9 = models.DecimalField(decimal_places=2)
      ip = models.DecimalField(decimal_places=1)
      so = models.IntegerField()
      so9 = models.DecimalField(decimal_places=1)
      sv = models.IntegerField()
      vorp = models.DecimalField(decimal_places=1)
      warp = models.DecimalField(decimal_places=2)
      whip = models.DecimalField(decimal_places=2)
      