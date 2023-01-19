from django.urls import path, include
from rest_framework import routers

from api.views.product_view_set import ProductViewSet
from api.views.stock_view_set import StockViewSet
from api.views.vending_machine_view_set import VendingMachineViewSet

router = routers.DefaultRouter()
router.register(r'vending-machine', VendingMachineViewSet)
router.register(r'product', ProductViewSet)
router.register(r'stock', StockViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
