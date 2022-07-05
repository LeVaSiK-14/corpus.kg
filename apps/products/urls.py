from rest_framework.routers import DefaultRouter as DR
from apps.products.views import(
    ProductModelViewSet, CategoryModelViewSet,
    SubCategoryModelViewSet, SetModelViewSet,
    ColorModelViewSet, FabricModelViewSet,
    StockView, GoodCreditView
)
router = DR()

router.register('products', ProductModelViewSet, basename='product')
router.register('categories', CategoryModelViewSet, basename='category')
router.register('sub_categories', SubCategoryModelViewSet, basename='sub_category')
router.register('sets', SetModelViewSet, basename='set')
router.register('colors', ColorModelViewSet, basename='color')
router.register('fabrics', FabricModelViewSet, basename='fabric')

router.register('good_creadit', GoodCreditView, basename='good_creadit')
router.register('stock', StockView, basename='stock')

urlpatterns = []

urlpatterns += router.urls