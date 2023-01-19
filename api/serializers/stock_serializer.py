from rest_framework import serializers

from api.models.stock import Stock


class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'vending_machine', 'product', 'quantity')
