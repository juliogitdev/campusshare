# posts/forms.py
from django import forms
from .models import Comentario, Postagem

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto_comentario']
        widgets = {
            'texto_comentario': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Escreva seu comentário aqui...'
            }),
        }
        labels = {
            'texto_comentario': '' 
        }

class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = ['texto_conteudo', 'tags']
        widgets = {
            'texto_conteudo': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'O que você está pensando?'
            }),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }