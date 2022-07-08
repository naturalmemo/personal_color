from django.db import models

class Sample(models.Model):
    select = models.IntegerField
    img = models.ImageField(verbose_name='img', blank=True, null=True)