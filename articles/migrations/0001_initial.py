# Generated by Django 3.0.3 on 2020-02-17 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='título del artículo')),
                ('content', models.TextField(verbose_name='contenido del artículo')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(null=True, upload_to='media', verbose_name='imagen para el artículo')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
