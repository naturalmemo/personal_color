from unicodedata import name
from django.db import models
from numpy import size
# from config.settings import MEDIA_ROOT

# from config.settings_common import MEDIA_URL

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
    id = models.IntegerField(primary_key=id,null=False)
    name = models.CharField(max_length=10,null=False)
    base_doc = models.CharField(max_length=100)
    base_doc_spring = models.CharField(max_length=100)#季節の説明
    

class Colors(models.Model):
    Colors_id = models.IntegerField(primary_key=id,null=False)
    Colors_name = models.CharField(max_length=10,null=False)
    base_type_id = models.CharField(max_length=100)

class Items(models.Model):
    Items_id = models.IntegerField(primary_key=id)
    Item_color_id = models.IntegerField()
    Items_sex = models.IntegerField()
    Items_name = models.CharField(max_length=20,null=False)
    Items_explanaion = models.CharField(max_length=100,null=False)
    Items_price = models.IntegerField()
    Items_size = models.ImageField()
    Items_maker =  models.CharField(max_length=20)
