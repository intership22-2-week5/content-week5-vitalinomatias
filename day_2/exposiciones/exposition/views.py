from rest_framework.views import Response
from rest_framework import viewsets

#serializers
from .serializers import PortfolioSerializer, ExpositionSerializer, Exposition_PortfolioSerializer

#models
from .models import Portfolio, Exposition, Exposition_Portfolio

# Create your views here.

class PortfolioViewSet(viewsets.ModelViewSet):
  queryset = Portfolio.objects.all()
  serializer_class = PortfolioSerializer
  
class ExpositionViewSet(viewsets.ModelViewSet):
  queryset = Exposition.objects.all()
  serializer_class = ExpositionSerializer
  
class Exposition_PortfolioViewSet(viewsets.ModelViewSet):
  queryset = Exposition_Portfolio.objects.all()
  serializer_class = Exposition_PortfolioSerializer





