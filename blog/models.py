from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='nombre', max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado el')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created']

    def __str__(self) -> str:
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicacion', default=now())
    image = models.ImageField(verbose_name='Imagen' ,upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE, )
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self) -> str:
        return str(self.title)