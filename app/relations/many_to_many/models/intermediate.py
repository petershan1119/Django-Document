from datetime import datetime
from django.utils import timezone
from django.db import models

__all__ = (
    'Post',
    'User',
    'Postlike',
)


# Extra fields on many-to-many relationships
class Post(models.Model):
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(
        'User',
        through='Postlike',
        related_name='like_posts', # u2.post_set.all() 대신 u2.like_posts.all()
    )

    class Meta:
        verbose_name_plural = 'Intermediate - Posts'

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Intermediate - Users'

    def __str__(self):
        return self.name


class Postlike(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name_plural = 'Intermediate - Postlike'

    def __str__(self):
        return '"{title}"글의 좋아요({name}, {date})'.format(
            title=self.post.title,
            name=self.user.name,
            date=datetime.strftime(
                timezone.make_naive(self.created_date),
                '%Y.%m.%d'),
        )