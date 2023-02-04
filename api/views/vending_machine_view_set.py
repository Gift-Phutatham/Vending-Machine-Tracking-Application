from typing import Any

from rest_framework import viewsets

from api.models.vending_machine import VendingMachine
from api.serializers.vending_machine_serializer import VendingMachineSerializer


class VendingMachineView(viewsets.ModelViewSet):
    queryset: Any = VendingMachine.objects.all()
    serializer_class = VendingMachineSerializer
