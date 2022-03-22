
from django.contrib import admin
from catalog.models import Product

class Products(admin.ModelAdmin):
    list_display = ('id', 'sku', 'name', 'qtd', 'price', 'barcode', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Product, Products)

