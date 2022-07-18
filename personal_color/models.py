from tabnanny import verbose
from django.db import models
#from accounts.models import CustomUser

CHOICES = [
    (1, '女性'),
    (2, '男性'),
    (3, 'その他'),
    (4, '無回答')
]

class Sample(models.Model):
    gender = models.CharField(verbose_name='gender', choices=CHOICES, blank=False, null=False, max_length=100, default=1)
    img = models.ImageField(verbose_name='img', blank=False, null=False)

    def __str__(self):
        return str(self.gender)


class Base_type(models.Model):
    #ベースタイプテーブルの作成
    name = models.CharField(verbose_name='季節', max_length=10)
    base = models.CharField(verbose_name='ベースタイプ', max_length=10)
    base_doc = models.CharField(verbose_name='ベース説明', max_length=100)
    color_doc = models.CharField(verbose_name='色の説明', max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'ベースタイプ'


class Colors(models.Model):
    #色テーブルの作成
    name = models.CharField(verbose_name='色名', max_length=20)
    img = models.ImageField(verbose_name='色の画像')
    base_type = models.ForeignKey(Base_type, verbose_name='ベースタイプ', related_name='co_base', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = '色'


class Items(models.Model):
    #アイテムテーブルの作成
    name = models.CharField(verbose_name='アイテム名', max_length=20)
    img = models.ImageField(verbose_name='アイテム画像')
    gender = models.IntegerField(verbose_name='性別')
    color = models.ForeignKey(Colors, verbose_name='色名', related_name='itm_color', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'アイテム'