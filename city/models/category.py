from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name
