from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = Elasticsearch()

product = Product(
    sku="SG-S22-5G-BL",
    name="Galaxy S22 Ultra 5G",
    qtd=10,
    price="7884.90",
    barcode="7892509122580",
    type=2,
    description="Smartphone Samsung Galaxy S22 Ultra 12GB RAM Rosa"
)
product.save()

s = ProductDocument.search().query("match", description="Rosa")

for hit in s:
    print("Product name : {}, description {}".format(hit.name, hit.description))
