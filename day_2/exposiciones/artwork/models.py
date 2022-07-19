from django.db import models

#models Portfolio
from exposition.models import Portfolio

# Create your models here.

class Type(models.Model):
  name = models.CharField(max_length=50)
  status = models.BooleanField(default=True)
  
  def __str__(self):
    return f'{self.name}'
  

class Author(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  status = models.BooleanField(default=True)
  
  def __str__(self):
    return f'{self.first_name} - {self.last_name}'
  
class Artwork(models.Model):
  type_artwork = models.ForeignKey(Type, on_delete=models.CASCADE)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  date = models.DateField()
  cost = models.CharField(max_length=10)
  attached = models.CharField(max_length=50)
  portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
  status = models.BooleanField(default=True)
  
  def __str__(self):
    return f'{self.type_artwork} - {self.author}'