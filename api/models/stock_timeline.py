from django.db import models
from django.db.models import AutoField, DateTimeField, PositiveIntegerField
from django.utils import timezone

from api.models.product import Product
from api.models.vending_machine import VendingMachine


class StockTimeline(models.Model):
    """Stock Timeline model, related to Stock."""

    id: AutoField = models.AutoField(primary_key=True)
    vending_machine: VendingMachine = models.ForeignKey(VendingMachine, on_delete=models.DO_NOTHING)
    product: Product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity: PositiveIntegerField = models.PositiveIntegerField()
    timestamp: DateTimeField = models.DateTimeField(default=timezone.now)
