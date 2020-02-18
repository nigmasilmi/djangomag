from django.db import models


class Publicidad(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Título de la publicidad', null=True, blank=False)
    client = models.CharField(
        max_length=255, verbose_name='Nombre del cliente', null=True, blank=False)
    ad_728por90 = models.ImageField(
        upload_to='pub_imgs/', verbose_name='imagen publicidad 720x90 px', blank=False, null=True)
    ad_300por250 = models.ImageField(
        upload_to='pub_imgs/', verbose_name='imagen publicidad 300x250 px', blank=False, null=True)

    def __str__(self):
        title = self.title
        client = self.client
        info = f'{title} de {client}'
        return info
