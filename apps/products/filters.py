import django_filters

from apps.products.models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Product
        fields = ["subcategory", "prod_set", "price", "name"]