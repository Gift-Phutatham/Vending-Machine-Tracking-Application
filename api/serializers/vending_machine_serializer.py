from rest_framework import serializers

from api.models.vending_machine import VendingMachine


class VendingMachineSerializer(serializers.ModelSerializer):
    """Vending Machine serializer."""

    class Meta:
        model = VendingMachine
        fields: tuple[str, str, str, str] = ("id", "name", "location", "is_active")
