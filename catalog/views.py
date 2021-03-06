from rest_framework import viewsets
from catalog.models import Product
from catalog.serializer import ProductSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer