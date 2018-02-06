from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)


class TwitterUser(models.Model):
    """
    Block기능 있어야 함
    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+',
    )

    class Meta:
        verbose_name_plural = 'Symmetrical_intermediate - TwitterUsers'

    def __str__(self):
        return self.name

    @property
    def following(self):
        following_relations = self.relations_by_from_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING,
        )
        following_pk_list = following_relations.values_list('to_user', flat=True)
        following_users = TwitterUser.objects.filter(pk__in=following_pk_list)
        return following_users

    @property
    def followers(self):
        followers_relations = self.relations_by_to_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING,
        )
        followers_pk_list = followers_relations.values_list('from_user', flat=True)
        followers_users = TwitterUser.objects.filter(pk__in=followers_pk_list)
        return followers_users

    @property
    def block_users(self):
        """
        block하고 있는 TwitterUser목록
        """
        block_relations = self.relations_by_from.filter(
            type=Relation.RELATION_TYPE_BLOCK,
        )
        block_pk_list = block_relations.values_list('to_user', flat=True)
        block_users = TwitterUser.objects.filter(pk__in=block_pk_list)
        return block_users


    def is_followee(self, to_user):
        """
        내가 to_user를 follow하고 있는지 여부를 True/False
        """
        return self.following.filter(pk=to_user.pk).exists()

    def is_follower(self, from_user):
        """
        from_user가 나를 follow하고 있는지 여부를 True/False
        """
        return self.following.filter(pk=from_user.pk).exists()


    def follow(self, to_user):
        """
        to_user에 주어진 TwitterUser를 follow함
        """
        self.relations_by_from_user.create(
            # from_user=self,
            to_user=to_user,
            type=Relation.RELATION_TYPE_FOLLOWING,
        )
        # Relation.objects.create(
        #     from_user=self,
        #     to_user=to_user,
        #     type=Relation.RELATION_TYPE_FOLLOWING,
        # )


    def block(self, to_user):
        self.reations_by_from_user.filter(to_user=to_user).delete()
        self.relations_by_from_user.create(
            # from_user=self,
            to_user=to_user,
            type=Relation.RELATION_TYPE_BLOCK,
        )

class Relation(models.Model):
    """
    유저간의 관계를 정의하는 모델
    단순히 자신의 MTM이 아닌 중개모델의 역할을 함
    추가적으로 받는 정보는 관계의 타입(팔로잉 또는 차단)
    """
    RELATION_TYPE_FOLLOWING = 'f'
    RELATION_TYPE_BLOCK = 'b'
    CHOICES_TYPE = (
        (RELATION_TYPE_FOLLOWING, '팔로잉'),
        (RELATION_TYPE_BLOCK, '차단'),
    )

    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 from_user인 경우에 Relation목록을 가져오고 싶을 경우
        related_name='relations_by_from_user',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 to_user인 경우에 Relation목록을 가져오고 싶을 경우
        related_name='relations_by_to_user',
    )
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)
    # modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            # from_user와 to_user의 값이 이미 있을 경우
            # DB에 중복 데이터 저장을 막음
            # ex) from_user가 1, to_user가 3인 데이터가 이미 있다면,
            # 두 항목의 값이 모두 같은 또 다른 데이터가 존재할 수 없음
            ('from_user', 'to_user'),
        )
        verbose_name_plural = 'Symmetrical_intermediate - TwitterUsers'