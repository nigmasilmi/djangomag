from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from . modelsMore import Categoria


class News(models.Model):
    title = models.CharField(
        max_length=200, verbose_name='título del artículo', null=True, blank=False)
    content = models.TextField(verbose_name='contenido del artículo')
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='art_imgs/', verbose_name='imagen para el artículo', blank=False, null=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        creator = self.author
        title = self.title
        identification = f'{title} publicado por {creator}'
        return identification
