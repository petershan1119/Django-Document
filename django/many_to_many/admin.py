from django.contrib import admin

from .models import Topping, Pizza, Post, User, Postlike

admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Postlike)