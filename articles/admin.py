from django.contrib import admin
from . models import News
from . modelsMore import Categoria

admin.site.register(News)
admin.site.register(Categoria)

# Register your models here.
