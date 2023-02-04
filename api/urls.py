from typing import List

from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from api.views.product_view_set import ProductViewSet
from api.views.stock_view_set import StockViewSet
from api.views.vending_machine_view_set import VendingMachineViewSet

router: DefaultRouter = routers.DefaultRouter()
router.register(r'vending-machine', VendingMachineViewSet)
router.register(r'product', ProductViewSet)
router.register(r'stock', StockViewSet)

urlpatterns: List = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
