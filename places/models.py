from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название места')
    slug = models.CharField(max_length=50, blank=True)
    description_short = models.TextField(verbose_name='Короткое описание', blank=True)
    description_long = HTMLField(verbose_name='Полное описание', blank=True)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='media/')
    place = models.ForeignKey(Place, verbose_name='Место', related_name='images', on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='Позиция', default=0)

    def __str__(self):
        return f'{self.place}, {self.number}'
