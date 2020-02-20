from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название компании")
    address = models.CharField(max_length=352, verbose_name="Адрес компании")

    def __str__(self):
        return self.title