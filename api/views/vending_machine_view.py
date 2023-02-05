from typing import Any

from rest_framework import viewsets

from api.models.vending_machine import VendingMachine
from api.serializers.vending_machine_serializer import VendingMachineSerializer


class VendingMachineView(viewsets.ModelViewSet):
    """
    Create: Create a new vending machine instance.

    Retrieve: Return the existing vending machine.

    Update: Update the existing vending machine.

    Destroy: Delete the existing vending machine.

    List: Return a list of all the existing vending machine.
    """

    queryset: Any = VendingMachine.objects.all()
    serializer_class = VendingMachineSerializer
