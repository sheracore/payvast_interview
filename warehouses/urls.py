from rest_framework.routers import DefaultRouter

from .api.views import WarehouseViewSet, GoodViewSet

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet, basename='warehouses')
router.register(r'goods', GoodViewSet, basename='goods')

warehouse_urlpatterns = router.urls