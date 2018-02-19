from django.db import models

__all__ = (
    'Topping',
    'Pizza',
)


class Topping(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Basic - Toppings'

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    class Meta:
        verbose_name_plural = 'Basic - Pizzas'

    def __str__(self):
        return self.name