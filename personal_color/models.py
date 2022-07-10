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
    gender = models.CharField(verbose_name='gender', choices=CHOICES, blank=False, null=False, max_length=100, default=1)
    img = models.ImageField(upload_to='media/', verbose_name='img', blank=False, null=False)

    def __str__(self):
        return str(self.gender)