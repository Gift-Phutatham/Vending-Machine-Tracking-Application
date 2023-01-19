from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name
