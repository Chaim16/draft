from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    id = models.BigAutoField(primary_key=True)
    nickname = models.CharField(max_length=64, null=True)
    gender = models.IntegerField(default=0, null=True)
    phone = models.CharField(max_length=32, null=True)
    is_ban = models.IntegerField(default=0)
    role = models.CharField(max_length=20)
    balance = models.FloatField(default=0.00)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username


class Order(models.Model):

    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    amount = models.FloatField()
    status = models.CharField(max_length=20)
    draft_id = models.BigIntegerField()
    create_time = models.BigIntegerField()
    is_cancel = models.IntegerField()
    cancel_time = models.BigIntegerField()

    class Meta:
        db_table = 'order'


class Category(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)


class Draft(models.Model):

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=2048)
    price = models.FloatField()
    category_id = models.BigIntegerField()
    designer_id = models.BigIntegerField()
    status = models.CharField(max_length=20)
    online_time = models.BigIntegerField()
    is_outline = models.IntegerField(default=0)

    class Meta:
        db_table = 'draft'


class Browse(models.Model):

    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    draft_id = models.BigIntegerField()

    class Meta:
        db_table = 'browse'

