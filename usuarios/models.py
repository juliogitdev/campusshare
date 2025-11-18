from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    # Relacionamento (1,1) - "Um usuário possui um perfil"
    # Onde delete=models.CASCADE significa: se deletar o usuário, apaga o perfil junto.
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')

    # Campos baseados no seu diagrama
    instituicao = models.CharField(max_length=150, blank=True, null=True)
    curso = models.CharField(max_length=100, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    
    # No diagrama está 'username'. O User padrão já tem username de login.
    # Aqui criamos um 'nome_exibicao' caso queira um nome diferente do login.
    nome_exibicao = models.CharField(max_length=50, blank=True, null=True)

    # No diagrama está 'foto_url'. No Django usamos ImageField.
    # Ele salva a imagem e gera a URL automaticamente.
    foto = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"