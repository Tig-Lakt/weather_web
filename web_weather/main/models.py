from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название города")
    mention_count = models.PositiveIntegerField(default=0, verbose_name="Количество упоминаний")

    def __str__(self):
        return f"{self.name} ({self.mention_count})"
