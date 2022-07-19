#django rest framework
from rest_framework import serializers

#models
from .models import Portfolio, Exposition, Exposition_Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Portfolio
    fields = '__all__'
    
class ExpositionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Exposition
    fields = '__all__'
    
class Exposition_PortfolioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Exposition_Portfolio
    fields = '__all__'
    
  def to_representation(self, instance):
    return {
      'id': instance.id,
      'exposition': instance.exposition.name,
      'portfolio': instance.portfolio.name
    }