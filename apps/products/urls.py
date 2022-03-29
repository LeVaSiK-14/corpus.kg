from rest_framework.routers import SimpleRouter
from apps.products.views import(
    ProductModelViewSet, CategoryModelViewSet,
    SubCategoryModelViewSet, SetModelViewSet,
    ColorModelViewSet, FabricModelViewSet
)
router = SimpleRouter()

router.register('products', ProductModelViewSet, basename='product')
router.register('categories', CategoryModelViewSet, basename='category')
router.register('sub_categories', SubCategoryModelViewSet, basename='sub_category')
router.register('sets', SetModelViewSet, basename='set')
router.register('colors', ColorModelViewSet, basename='color')
router.register('fabrics', FabricModelViewSet, basename='fabric')

urlpatterns = []

urlpatterns += router.urls