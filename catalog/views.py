from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import serializers
from catalog.models import Product
from django.views.decorators.cache import cache_page


class ProductsViewSet(viewsets.ModelViewSet):

    @cache_page(60*15)
    def list_all(request):
        queryset = Product.objects.all()
        return Response(request)
