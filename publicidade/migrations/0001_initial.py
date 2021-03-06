# Generated by Django 3.0.3 on 2020-02-18 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Título de la publicidad')),
                ('client', models.CharField(max_length=255, null=True, verbose_name='Nombre del cliente')),
                ('ad_728por90', models.ImageField(null=True, upload_to='pub_imgs/', verbose_name='imagen publicidad 720x90 px')),
                ('ad_300por250', models.ImageField(null=True, upload_to='pub_imgs/', verbose_name='imagen publicidad 300x250 px')),
            ],
        ),
    ]
