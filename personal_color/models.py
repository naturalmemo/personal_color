from unicodedata import name
from django.db import models
from numpy import size
from config.settings import MEDIA_ROOT

from config.settings_common import MEDIA_URL

from django.db import models

CHOICES = [
    (1, '女性'),
    (2, '男性'),
    (3, 'その他'),
    (4, '無回答')
]

class Sample(models.Model):
    gender = models.CharField(verbose_name='gender', choices=CHOICES, blank=False, null=False, max_length=100, default=1)
    img = models.ImageField(upload_to='media/', verbose_name='img', blank=False, null=False)

    def __str__(self):
        return str(self.gender)





class Base_type(models.Model):
    base_type_id = models.IntegerField()
    base_type_name = models.CharField(max_length=10,null=True)
    base_type_base_doc = models.CharField(max_length=20)

class Colors(models.Model):
    Colors_id = models.IntegerField()
    Colors_name = models.CharField(max_length=10,null=True)
    Colors_id = models.IntegerField()

class Items(models.Model):
    Items_id = models.IntegerField()
    Items_sex = models.IntegerField()
    Items_name = models.CharField(max_length=20,null=True)
    Items_explanate = models.CharField(max_length=100,null=True)
    Items_price = models.IntegerField()
    Items_size = models.ImageField()
    Items_maker =  models.CharField(max_length=20)
