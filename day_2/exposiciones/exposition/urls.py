## django rest framework

#django
from django.urls import path
from django.db import router


#rest framework
from rest_framework.routers import DefaultRouter

#views
from .views import PortfolioViewSet, ExpositionViewSet, Exposition_PortfolioViewSet

# instancia de default raouter
router = DefaultRouter()

router.register(r'portfolio', PortfolioViewSet)
router.register(r'exposition', ExpositionViewSet)
router.register(r'exposition_portfolio', Exposition_PortfolioViewSet)

urlpatterns = router.urls

urlpatterns += [
    
]
