from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = models.FileField(upload_to="category_image", blank=True, verbose_name="Картинка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"