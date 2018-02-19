from django.contrib import admin

from .models import Manufacturer, Car, Person, Type, Pokemon

admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Person)
admin.site.register(Type)
admin.site.register(Pokemon)