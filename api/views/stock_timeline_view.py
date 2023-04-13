from typing import Any

from rest_framework import viewsets

from api.models.stock_timeline import StockTimeline
from api.serializers.stock_timeline_serializer import StockTimelineSerializer


class StockTimelineView(viewsets.ModelViewSet):
    """
    Create: Create a new stock timeline instance.

    Retrieve: Return the existing stock timeline.

    Update: Update the existing stock timeline.

    Destroy: Delete the existing stock timeline.

    List: Return a list of all the existing stock timelines.
    """

    queryset: Any = StockTimeline.objects.all()
    serializer_class = StockTimelineSerializer
