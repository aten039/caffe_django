from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name='Clave', max_length=100, unique=True)
    name = models.CharField(verbose_name='Red social', max_length=200 ) 
    url = models.URLField(verbose_name='Enlace', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces a RS'
        ordering = ['name'] 

    def __str__(self) -> str:
        return str(self.name)