from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import AutoField, CharField, DecimalField


class Product(models.Model):
    """
    Product model.
    """

    id: AutoField = models.AutoField(primary_key=True)
    name: CharField = models.CharField(max_length=100, unique=True)
    cost: DecimalField = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
