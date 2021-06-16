from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register(r'productos', viewsets.ProductoViewSet, basename="productos")

urlpatterns= router.urls