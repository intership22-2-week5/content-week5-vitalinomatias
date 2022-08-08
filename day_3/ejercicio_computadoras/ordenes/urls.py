from django.db import router
from django.urls import path

from rest_framework.routers import DefaultRouter

#views
from .views import RatonViewSet, TecladoViewSet, MonitorViewSet, AltavozViewSet, ProcesadorViewSet, PlacaViewSet, ComputadoraViewSet, OrdenViewSet, DetalleOrdenViewSet, ListarDispositivos

router = DefaultRouter()

router.register(r'raton', RatonViewSet)
router.register(r'teclado', TecladoViewSet)
router.register(r'monitor', MonitorViewSet)
router.register(r'altavoz', AltavozViewSet)
router.register(r'procesador', ProcesadorViewSet)
router.register(r'placa', PlacaViewSet)
router.register(r'computadora', ComputadoraViewSet)
router.register(r'orden', OrdenViewSet)
router.register(r'detalleorden', DetalleOrdenViewSet)



urlpatterns = router.urls

urlpatterns += [
    path('dispositivos/', ListarDispositivos.as_view({'get': 'list'})),    
]
