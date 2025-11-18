# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    nome_tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome_tag

class Postagem(models.Model):
    #(1,N) - Um usuário publica várias postagens
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postagens')
    

    texto_conteudo = models.TextField(verbose_name="Conteúdo")
    data_publicacao = models.DateTimeField(auto_now_add=True)

    #(N,N) - Postagem possui Tags
    tags = models.ManyToManyField(Tag, blank=True)

    #(N,N) - Usuário curte Postagens
    likes = models.ManyToManyField(User, related_name='postagens_curtidas', blank=True)

    def __str__(self):
        return f"Post de {self.autor.username} em {self.data_publicacao}"

    # Métod para contar curtidas
    def total_likes(self):
        return self.likes.count()

class Comentario(models.Model):
    #(1,N) - Usuário escreve comentários
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    # O comentário precisa pertencer a uma postagem específica.
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='comentarios')
    
    
    texto_comentario = models.TextField(verbose_name="Comentário")
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} na postagem {self.postagem.id}"