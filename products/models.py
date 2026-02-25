from django.db import models


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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"