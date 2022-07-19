#django rest framework
from rest_framework import serializers

#models
from .models import Type, Author,Artwork
from exposition.models import Portfolio

class TypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Type
    fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = '__all__'

class ArtworkSerializer(serializers.ModelSerializer):
  
  # type_artwork = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())
  type_artwork = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())
  author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
  portfolio = serializers.PrimaryKeyRelatedField(queryset=Portfolio.objects.all())
  class Meta:
    model = Artwork
    fields = '__all__'
  
  def to_representation(self, instance):
    return {
      'id': instance.id,
      'type_artwork': instance.type_artwork.name,
      'author': {
        'first_name': instance.author.first_name,
        'last_name': instance.author.last_name
      },
      'portfolio': instance.portfolio.name,
      'date': instance.date,
      'cost': instance.cost,
      'attached': instance.attached,
      'status': instance.status
    }