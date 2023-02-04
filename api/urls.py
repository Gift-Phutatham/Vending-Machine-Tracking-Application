from typing import List

from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from api.views.product_view_set import ProductView
from api.views.stock_view_set import StockView
from api.views.vending_machine_view_set import VendingMachineView

router: DefaultRouter = routers.DefaultRouter()
router.register(r'vending-machine', VendingMachineView)
router.register(r'product', ProductView)
router.register(r'stock', StockView)

urlpatterns: List = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
