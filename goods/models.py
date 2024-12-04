from django.db import models
from django.urls import reverse

# Create your models here.  


class Category(models.Model):

    name = models.CharField(max_length=150, unique=True, verbose_name = "Название товара")
    slug = models.SlugField(max_length=250, unique=True, blank = True, null = True, verbose_name = "URL каталога")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"


class Product(models.Model):

    name = models.CharField(max_length=150, unique = True, verbose_name = "Имя Товара")
    description = models.TextField(unique=False, blank=True, null=True, verbose_name="Описание товара")
    slug = models.SlugField(max_length=250 ,unique=True , blank=True, null=True, verbose_name="URL продукта")
    image = models.ImageField(upload_to="goods_media", blank=True, null=True, verbose_name= "Картинка товара")
    price = models.DecimalField(max_digits=7, default=0, decimal_places=2, blank=True, null=True, verbose_name="Цена товара")
    count = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, verbose_name="Категория", related_name="product_category")

    class Meta:
        db_table = "product"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("id", )

    def __str__(self):
        return self.name
    
    def id_product(self):
        return f"{self.id:06}" #"000012"
    
    
    
