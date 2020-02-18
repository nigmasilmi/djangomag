from django.db import models


class Categoria(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='nombre de la categoría', null=True, blank=False)

    def __str__(self):
        return self.name
