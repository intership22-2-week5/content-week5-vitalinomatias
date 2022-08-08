from rest_framework import serializers

from .models import Raton, Teclado, Monitor, Altavoz, Procesador, Placa, Computadora, Orden, DetalleOrden

class RatonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Raton
        fields = '__all__'
        
class TecladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teclado
        fields = '__all__'
    
class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'
        
class AltavozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Altavoz
        fields = '__all__'
        
class ProcesadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procesador
        fields = '__all__'
        
class PlacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placa
        fields = '__all__'
        
class ComputadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computadora
        fields = '__all__'
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'cantidad': instance.cantidad,
            'costo': instance.costo,
            'fecha_ingreso': instance.fecha_ingreso,
            'raton': {
                'id': instance.raton.id,
                'tipo': instance.raton.tipo,
                'marca': instance.raton.marca
            },
            'teclado': {
                'id': instance.teclado.id,
                'tipo': instance.teclado.tipo,
                'marca': instance.teclado.marca
            },
            'monitor': {
                'id': instance.monitor.id,
                'tipo': instance.monitor.tipo,
                'marca': instance.monitor.marca
            },
            'altavoz': {
                'id': instance.altavoz.id,
                'tipo': instance.altavoz.tipo,
                'marca': instance.altavoz.marca
            },
            'procesador': {
                'id': instance.procesador.id,
                'tipo': instance.procesador.tipo,
                'marca': instance.procesador.marca
            },
            'placa': {
                'id': instance.placa.id,
                'tipo': instance.placa.tipo,
                'marca': instance.placa.marca
            }
        }
        
class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'
        
class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrden
        fields = '__all__'