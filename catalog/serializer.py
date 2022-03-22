from rest_framework import serializers
from catalog.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'qtd', 'price', 'barcode', 'description']