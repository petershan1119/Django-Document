from django.contrib import admin

from .models import (
    # basic
    Topping, Pizza,
    # intermediate
    Post, User, Postlike,
    # self
    FacebookUser, InstagramUser, TwitterUser, Relation
)

admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Postlike)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)
admin.site.register(TwitterUser)
admin.site.register(Relation)