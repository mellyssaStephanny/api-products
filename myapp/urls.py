from django.contrib import admin
from django.urls import path, include
from catalog.views import ProductsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
