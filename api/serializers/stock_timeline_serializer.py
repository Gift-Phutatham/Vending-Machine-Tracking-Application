from rest_framework import serializers

from api.models.stock_timeline import StockTimeline


class StockTimelineSerializer(serializers.ModelSerializer):
    """Stock Timeline serializer."""

    class Meta:
        model = StockTimeline
        fields: tuple[str, str, str, str, str] = ("id", "vending_machine", "product", "quantity", "timestamp")
