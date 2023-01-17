from rest_framework import serializers

from .models import VendingMachine


class VendingMachineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VendingMachine
        fields = ('name', 'location')
