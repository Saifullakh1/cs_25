from django.db import models

from accounts.models import Account
from categories.models import Category


class Currency(models.Choices):
    dollar = 'dollar'
    som = 'som'
    euro = 'euro'


class Color(models.Choices):
    black = 'black'
    white = 'white'
    yellow = 'yellow'
    green = 'green'


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.IntegerField(default=0, verbose_name="Цена")
    currency = models.CharField(max_length=20, choices=Currency.choices, default=Currency.som, verbose_name="Валюта")
    image = models.ImageField(upload_to="product_images", blank=True, verbose_name="Картинка")
    color = models.CharField(max_length=20, choices=Color.choices, verbose_name="Цвет")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"



class Favorite(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user_favorites")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_favorites")

    def __str__(self):
        return f"{self.user} - {self.product}"

    class Meta:
        verbose_name = "Избранный"
        verbose_name_plural = "Избранные"
        unique_together = ("user", "product")