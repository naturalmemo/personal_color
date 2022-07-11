from django.db import models
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
    ID = models.IntegerField()
    NAME = models.CharField(max_length=10)
    BASE_DOC = models.CharField(max_length=20)
    
class Colors(models.Model):
    ID = models.IntegerField()
    NAME = models.CharField(max_length=10)
    BASE_TYPE_ID = models.IntegerField()

class Items(models.Model):
    ID = models.IntegerField()
    COLOR_ID = models.IntegerField()
    SEX = models.IntegerField()
    NAME = models.CharField(max_length=20)
    EXPLANAION = models.CharField(max_length=100)
    PRICE = models.IntegerField()
    SIZE = models.ImageField()
    MAKER =  models.CharField(max_length=20)
