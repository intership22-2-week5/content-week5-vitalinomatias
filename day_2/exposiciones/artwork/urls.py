## django rest framework

#django
from django.urls import path
from django.db import router


#rest framework
from rest_framework.routers import DefaultRouter

#views
from .views import TypeViewSet, AuthorViewSet, ArtworkViewSet

# instancia de default raouter
router = DefaultRouter()

router.register(r'type', TypeViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'artwork', ArtworkViewSet)


urlpatterns = router.urls

urlpatterns += [
    
]
