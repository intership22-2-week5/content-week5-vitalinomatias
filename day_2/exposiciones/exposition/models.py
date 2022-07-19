from pyexpat import model
from django.db import models

# Create your models here.

class Portfolio(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  status = models.BooleanField(default=True)
  
  def __str__(self):
    return f'{self.name}'
  
class Exposition(models.Model):
  name = models.CharField(max_length=50)
  date = models.DateField()
  locale = models.CharField(max_length=50)
  description = models.CharField(max_length=500)
  status = models.BooleanField(default=True)
  
  def __str__(self):
    return f'{self.name}'
  
class Exposition_Portfolio(models.Model):
  exposition = models.ForeignKey(Exposition, on_delete=models.CASCADE)
  portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'{self.expositon} - {self.portfolio}'