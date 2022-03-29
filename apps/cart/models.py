
from django.db import models
from apps.products.models import Product


class Order(models.Model):
    email = models.EmailField()
    addres = models.CharField(max_length=127, null=True, blank=True)
    full_name = models.CharField(max_length=127)
    phone = models.CharField(max_length=127)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    
    @property
    def sum_price(self):
        return self.amount*self.product.price
    
    @property
    def product_name(self):
        return self.product.name
    
    @property
    def product_price(self):
        return self.product.price

    def __str__(self):
        return f"#{self.amount} of {self.product.name}"
