from django.contrib import admin
# # Register your models here.

# モデルをインポート
from . models import Base_type

# 管理ツールに登録
admin.site.register(Base_type)