from rest_framework import serializers

from api.models.stock import Stock


class StockSerializer(serializers.ModelSerializer):
    """
    Stock serializer.
    """

    class Meta:
        model = Stock
        fields: tuple[str, str, str, str] = ('id', 'vending_machine', 'product', 'quantity')
