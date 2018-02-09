from django.db import models

class Other(models.Model):
    pass


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    other = models.ForeignKey(
        Other,
        on_delete=models.SET_NULL,
        related_name='places',
        related_query_name='place',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'Place {self.name} | {self.address}'

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    nearby_places = models.ManyToManyField(
        Place,
        related_query_name='near_restaurant',
    )

    def __str__(self):
        return f'Restaurant {self.name} | {self.serves_hot_dogs} | {self.serves_pizza}'