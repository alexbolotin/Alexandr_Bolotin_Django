from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.Genre)
admin.site.register(models.Book)
admin.site.register(models.Publishing_house)
admin.site.register(models.Author)
admin.site.register(models.Series)