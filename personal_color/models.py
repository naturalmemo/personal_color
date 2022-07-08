from django.db import models
from config.settings import MEDIA_ROOT

from config.settings_common import MEDIA_URL

CHOICES = [
    (1, '女性'),
    (2, '男性'),
    (3, 'その他'),
    (4, '無回答')
]

class Sample(models.Model):
    gender = models.TextField(verbose_name='gender', choices=CHOICES, blank=False, null=False)
    img = models.ImageField(upload_to='media/', verbose_name='img', blank=False, null=False)
