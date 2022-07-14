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
    season = models.CharField(max_length=10)
    base = models.CharField(max_length=10)
    img_path = models.CharField(max_length=10)
    base_type_txt = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'ベースタイプ'


class Colors(models.Model):
    #色テーブルの作成
    color = models.CharField(max_length=20)
    img_path = models.CharField(max_length=10)
    base_type_id = models.IntegerField()

    def __str__(self):
        return str(self.color)

    class Meta:
        verbose_name_plural = '色'


class Items(models.Model):
    #アイテムテーブルの作成

    gender = models.IntegerField()
    Items_name = models.CharField(max_length=20,null=False)
    img_path = models.CharField(max_length=10)
    color_id = models.IntegerField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'アイテム'