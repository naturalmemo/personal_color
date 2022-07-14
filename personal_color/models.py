from django.db import models

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