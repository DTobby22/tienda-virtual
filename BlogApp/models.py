from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __def__(self):
        return self.name


class Post(models.Model):
    Titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="blog", null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    Categoria = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = 'post'
        verbose_name_plural = 'Posts'

    def __def__(self):
        return self.name