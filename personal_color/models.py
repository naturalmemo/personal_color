from tabnanny import verbose
from django.db import models
from accounts.models import CustomUser

CHOICES = [
    (0, '女性'),
    (1, '男性'),
    (2, 'その他'),
    (3, '無回答')
]

class Sample(models.Model):
    gender = models.CharField(verbose_name='gender', choices=CHOICES, blank=False, null=False, max_length=100, default=0)
    img = models.ImageField(verbose_name='img', blank=False, null=False)

    def __str__(self):
        return str(self.gender)


class Base_type(models.Model):
    #ベースタイプテーブルの作成
    name = models.CharField(max_length=10)
    base = models.CharField(max_length=10)
    base_doc = models.CharField(max_length=100)
    color_doc = models.CharField(max_length=100)
    user_id = models.IntegerField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'ベースタイプ'


class Colors(models.Model):
    #色テーブルの作成
    name = models.CharField(max_length=20)
    path = models.CharField(max_length=30)
    base_type_id = models.IntegerField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = '色'


class Items(models.Model):
    #アイテムテーブルの作成

    path = models.CharField(max_length=30)
    gender = models.IntegerField()
    color_id = models.IntegerField()

    def __str__(self):
        return str(self.path)

    class Meta:
        verbose_name_plural = 'アイテム'