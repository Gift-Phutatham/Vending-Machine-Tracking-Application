from rest_framework import viewsets

from api.models.stock import Stock
from api.serializers.stock_serializer import StockSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
