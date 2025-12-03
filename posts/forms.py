# posts/forms.py
from django import forms
from .models import Comentario

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