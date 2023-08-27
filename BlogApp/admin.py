from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

# Aqui se configura el panel de administracion para usar los modelos del blog

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)