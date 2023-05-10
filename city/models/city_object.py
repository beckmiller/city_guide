from django.db import models


class CityObjects(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название заведения")
    description = models.TextField(verbose_name="Описание заведения")
    category = models.ForeignKey(
        "city.Category",
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Категория",
    )
    city = models.ForeignKey(
        "city.CityName",
        on_delete=models.CASCADE,
        related_name="cities",
        verbose_name="Город",
    )
    address = models.CharField(max_length=250, verbose_name="Адрес")
    address_number = models.IntegerField(verbose_name="Номер дома")
    contact = models.CharField(max_length=12, verbose_name="Номер телефона")

    class Meta:
        ordering = ["name"]
        verbose_name = "Городской бъект"
        verbose_name_plural = "Городские объекты"

    def __str__(self) -> str:
        return self.name
