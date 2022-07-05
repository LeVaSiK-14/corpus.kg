from django.contrib import admin
from apps.products.models import (
    Product, Category, Subcategory, 
    Set, Fabric, Colors, Stock, GoodCredit
)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Set)
admin.site.register(Fabric)
admin.site.register(Colors)

admin.site.register(Stock)
admin.site.register(GoodCredit)
