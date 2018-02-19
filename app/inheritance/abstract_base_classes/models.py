from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)


# Be careful with related_name and related_query_name
class Other(models.Model):
    pass


class Base(models.Model):
    other = models.ForeignKey(
        Other,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_set',
        related_query_name='%(app_label)s_%(class)s',
    )

    class Meta:
        abstract = True


class ChildA(Base):
    pass


class ChildB(Base):
    pass

# other = Other.objects.create()
# a1, a2, a3 = [ChildA.objects.create(other=other) for i in range(3)]
# other.abstract_base_classes_childa_set.all()
# Other.objects.all().filter(abstract_base_classes_childa__pk__gt=1)