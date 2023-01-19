from rest_framework import viewsets

from api.models.product import Product
from api.serializers.product_serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
