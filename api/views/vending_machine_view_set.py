from rest_framework import viewsets

from api.models.vending_machine import VendingMachine
from api.serializers.vending_machine_serializer import VendingMachineSerializer


class VendingMachineViewSet(viewsets.ModelViewSet):
    queryset = VendingMachine.objects.all().order_by('name')
    serializer_class = VendingMachineSerializer
