from typing import Any

from rest_framework import viewsets

from api.models.product import Product
from api.serializers.product_serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset: Any = Product.objects.all()
    serializer_class = ProductSerializer
