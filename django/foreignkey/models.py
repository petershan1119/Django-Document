from django.db import models


class Manufacturer(models.Model):
    name = models.CharField('제조사', max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )
    name = models.CharField('차종', max_length=60)

    def __str__(self):
        return f'{self.manufacturer.name} {self.name}'