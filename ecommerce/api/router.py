from rest_framework import routers
from api.viewsets import StoreViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'stores', StoreViewSet, basename='stores')
router.register(r'products', ProductViewSet, basename='products')

urls = router.urls
