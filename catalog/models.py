from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=13)
    qtd = models.IntegerField()
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    barcode = models.CharField(max_length=13) 
    description = models.TextField()
    type = models.IntegerField(choices=[
        (1, "TV"),
        (2, "Celular"),
        (4, "Notebook"),
    ])

    def __str__(self):
        return self.sku
