from django.db import models
from django.db.models import AutoField, CharField, BooleanField


class VendingMachine(models.Model):
    id: AutoField = models.AutoField(primary_key=True)
    name: CharField = models.CharField(max_length=100, unique=True)
    location: CharField = models.CharField(max_length=100)
    is_active: BooleanField = models.BooleanField(default=True)
