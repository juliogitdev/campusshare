from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    #(1,1) - "Um usuário possui um perfil"
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')

    instituicao = models.CharField(max_length=150, blank=True, null=True)
    curso = models.CharField(max_length=100, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    nome_exibicao = models.CharField(max_length=50, blank=True, null=True)

    foto = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"