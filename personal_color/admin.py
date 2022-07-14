from django.contrib import admin

from .models import Base_type, Colors, Items

admin.site.register(Base_type)
admin.site.register(Colors)
admin.site.register(Items)