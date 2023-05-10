from django.db import models


class CityName(models.Model):
    city_name = models.CharField(max_length=120)

    class Meta:
        ordering = ["city_name"]
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self) -> str:
        return self.city_name
