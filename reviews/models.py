from django.db import models
from products.models import Product
from accounts.models import Account


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_reviews")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account_reviews")
    rating = models.IntegerField(default=0, verbose_name="Оценка")
    comment = models.CharField(max_length=200, blank=True, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.rating}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"