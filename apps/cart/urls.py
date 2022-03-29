from rest_framework.routers import SimpleRouter

from apps.cart.views import (
    UserModelViewSet, OrderViewSet
)

router = SimpleRouter()

router.register('users', UserModelViewSet, basename='user')
router.register('order', OrderViewSet, basename='order')

urlpatterns = []

urlpatterns += router.urls