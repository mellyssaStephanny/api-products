from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from catalog.views import ProductsViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet)
#router.register(r'products', ProductsViewSet, basename='Products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
