from django.contrib import admin
from .models import Postagem, Comentario, Tag 

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('texto_conteudo', 'autor', 'data_publicacao') 


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'postagem', 'data_comentario')

admin.site.register(Tag)