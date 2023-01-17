from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VendingMachineSerializer
from .models import VendingMachine


class VendingMachineViewSet(viewsets.ModelViewSet):
    queryset = VendingMachine.objects.all().order_by('name')
    serializer_class = VendingMachineSerializer
