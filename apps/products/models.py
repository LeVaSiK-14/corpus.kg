from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='catgories/images')
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='subcategories/images', blank=True, null=True)
    
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return self.name


class Set(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Комлект"
        verbose_name_plural = "Комплекты"

    def __str__(self):
        return self.name


class Colors(models.Model):
    color_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self):
        return self.color_name


class Fabric(models.Model):
    fabric_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.fabric_name


class Product(models.Model):
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, 
        verbose_name="Подкатегория"
    )
    prod_set = models.ForeignKey(
        Set, on_delete=models.SET_NULL, blank=True, 
        null=True, verbose_name="Комплект"
    )
    name = models.CharField(
        max_length=255, verbose_name="Название"
    )
    vendor_code = models.CharField(
        max_length=255, verbose_name="Артикул"
    )
    color = models.ForeignKey(
        Colors, on_delete=models.SET_NULL, 
        null=True, verbose_name="Цвет"
    )
    fabric = models.ForeignKey(
        Fabric, on_delete=models.SET_NULL, 
        null=True, verbose_name="Материал"
    )
    price = models.DecimalField(
        decimal_places=2, default=0, 
        max_digits=20, verbose_name="Цена"
    )
    discount = models.PositiveIntegerField(
        default=0, verbose_name="Размер Скидки"
    )
    sale = models.BooleanField(
        default=False, verbose_name="На Скидке"
    )
    hit = models.BooleanField(
        default=False, verbose_name="Хит Продаж"
    )
    is_new = models.BooleanField(default=False, verbose_name='Новый', null=True)
    image = models.ImageField(
        upload_to="products/images"
    )
    image2 = models.ImageField(
        upload_to="products/images", blank=True, null=True
    )
    image3 = models.ImageField(
        upload_to="products/images", blank=True, null=True
    )
    image4 = models.ImageField(
        upload_to="products/images", blank=True, null=True
    )
    image5 = models.ImageField(
        upload_to="products/images", blank=True, null=True
    )
    image6 = models.ImageField(
        upload_to="products/images", blank=True, null=True
    )
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()

    @property
    def discount_price(self):
        if self.sale:
            return (self.price * (100 - self.discount) / 100)
        return self.price

    class Meta:
        ordering = ("date_added", )
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
