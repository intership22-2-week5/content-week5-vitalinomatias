from rest_framework.views import Response
from rest_framework import viewsets

#serializers
from .serializers import TypeSerializer, AuthorSerializer, ArtworkSerializer

#models
from .models import Type, Author, Artwork

# Create your views here.

class TypeViewSet(viewsets.ModelViewSet):
  queryset = Type.objects.all()
  serializer_class = TypeSerializer
  
class AuthorViewSet(viewsets.ModelViewSet):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer

class ArtworkViewSet(viewsets.ModelViewSet):
  queryset = Artwork.objects.all()
  serializer_class = ArtworkSerializer
