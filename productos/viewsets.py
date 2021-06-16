from rest_framework import viewsets

from .serializers import ProductosSerializer
from .models import Producto
from rest_framework.permissions import IsAuthenticated

class ProductoViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProductosSerializer
    queryset = Producto.objects.all()
    is_authenticated = [IsAuthenticated]