from urllib import response
from rest_framework import viewsets, generics
from rest_framework.views import Response
from django.forms import ValidationError

#serializers
from .serializers import RatonSerializer, TecladoSerializer, MonitorSerializer, AltavozSerializer, ProcesadorSerializer, PlacaSerializer, ComputadoraSerializer, OrdenSerializer, DetalleOrdenSerializer

#models
from .models import Raton, Teclado, Monitor, Altavoz, Procesador, Placa, Computadora, Orden, DetalleOrden

# Create your views here.

class RatonViewSet(viewsets.ModelViewSet):
    queryset = Raton.objects.all()
    serializer_class = RatonSerializer
    
class TecladoViewSet(viewsets.ModelViewSet):
    queryset = Teclado.objects.all()
    serializer_class = TecladoSerializer
    
class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
    
class AltavozViewSet(viewsets.ModelViewSet):
    queryset = Altavoz.objects.all()
    serializer_class = AltavozSerializer

class ProcesadorViewSet(viewsets.ModelViewSet):
    queryset = Procesador.objects.all()
    serializer_class = ProcesadorSerializer

class PlacaViewSet(viewsets.ModelViewSet):
    queryset = Placa.objects.all()
    serializer_class = PlacaSerializer

class ComputadoraViewSet(viewsets.ModelViewSet):
    queryset = Computadora.objects.all()
    serializer_class = ComputadoraSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({"message": e.message, "status": False})
        # if pc.data['id'] is not None:
        #     return pc
        # else:
        #     return Response({'message': 'falta stock'})

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    

class DetalleOrdenViewSet(viewsets.ModelViewSet):
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer


class ListarDispositivos(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    
    def listado_componentes(self):
        componentes = {
            'Raton': (Raton, RatonSerializer),
            'Teclado': (Teclado, TecladoSerializer),
            'Monitor': (Monitor, MonitorSerializer),
            'Altavoz': (Altavoz, AltavozSerializer),
            'Procesador': (Procesador, ProcesadorSerializer),
            'Placa': (Placa, PlacaSerializer)
        }
        
        return componentes
        
    
    def list(self, request, *args, **kwargs):
        dispositivo = self.request.query_params.get('dispositivo')
        marca = self.request.query_params.get('marca')

        print(dispositivo)
        print(marca)
        
        return self.busqueda_componente(dispositivo, marca)
    
    def busqueda_componente(self, dispositivo, marca):
        componentes = self.listado_componentes()
        
        try:
            for key, componente in componentes.items():
                if key == dispositivo:
                    return self.serialize_query(componente[0], componente[1], marca)
            
            return Response({'status': False, 'message': 'No existe ese dispositivo'})
        except Exception as e:
            return Response({'status': False, 'message': str(e)})
    
    
    def serialize_query(self, model, serializer, marca):
        queryset = model.objects.all()
        if marca is not None:
            queryset = queryset = model.objects.filter(marca=marca)
        serializer = serializer(queryset, many=True)
        return Response({'status': True, 'data':serializer.data})




class DispositoMarca(viewsets.ModelViewSet):
    
    def list(self, request, *args, **kwargs):
        dispositivoBusqueda = self.request.query_params.get('dispositivo')
        print(dispositivoBusqueda)