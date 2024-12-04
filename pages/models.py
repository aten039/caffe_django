from django.db import models

# Create your models here.

class Pages(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=100, unique=True)
    content = models.TextField(verbose_name='Contenido' ) 
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Politica'
        verbose_name_plural = 'Politicas'
        ordering = ['title'] 

    def __str__(self) -> str:
        return str(self.title)