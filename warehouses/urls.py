from rest_framework.routers import DefaultRouter

from .api.views import WarehouseViewSet

router = DefaultRouter()
router.register(r'warehouse', WarehouseViewSet, basename='warehouse')

warehouse_urlpatterns = router.urls