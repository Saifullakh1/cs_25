from django.db import models
from accounts.models import Account
from products.models import Product


class Cart(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="user_carts", verbose_name="Пользователь")
    product = models.ManyToManyField(Product, related_name="product_carts", verbose_name="Продукт")
    total = models.IntegerField(default=0, verbose_name="Сумма")

    def __str__(self):
        return f"{self.user} - {self.product}"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
