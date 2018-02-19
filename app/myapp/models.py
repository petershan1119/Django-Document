from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100, blank=True)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField(
        blank=True,
        null=True,
    )
    num_states = models.IntegerField()


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    # nickname = models.CharField(
    #     max_length=39,
    #     unique=True,
    # )
    shirt_size = models.CharField(
        max_length=1,
        choices=SHIRT_SIZES,
    )

    def __str__(self):
        return f'{self.name} (셔츠 사이즈: {self.get_shirt_size_display()})'