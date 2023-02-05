from typing import Any

from rest_framework import viewsets

from api.models.stock import Stock
from api.serializers.stock_serializer import StockSerializer


class StockView(viewsets.ModelViewSet):
    """
    Create: Create a new stock instance.

    Retrieve: Return the existing stock.

    Update: Update the existing stock.

    Destroy: Delete the existing stock.

    List: Return a list of all the existing stocks.
    """

    queryset: Any = Stock.objects.all()
    serializer_class = StockSerializer
