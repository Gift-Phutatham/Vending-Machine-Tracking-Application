from rest_framework import serializers

from api.models.stock import Stock


class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ('vending_machine', 'product', 'quantity')
