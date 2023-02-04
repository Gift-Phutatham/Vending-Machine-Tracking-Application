from typing import Any

from rest_framework import viewsets

from api.models.product import Product
from api.serializers.product_serializer import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    """
    Create:
    Create a new product instance.

    Retrieve:
    Return the existing product.

    Update:
    Update the existing product.

    Destroy:
    Delete the existing product.

    List:
    Return a list of all the existing products.
    """

    queryset: Any = Product.objects.all()
    serializer_class = ProductSerializer
