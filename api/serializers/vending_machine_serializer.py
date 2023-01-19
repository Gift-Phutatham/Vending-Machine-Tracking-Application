from rest_framework import serializers

from api.models.vending_machine import VendingMachine


class VendingMachineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VendingMachine
        fields = ('name', 'location', 'is_active')
