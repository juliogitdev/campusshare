from django import forms
from django.contrib.auth.models import User 
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm 

class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email'] 
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
        }

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['biografia', 'instituicao', 'curso'] 
        widgets = {
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Conte um pouco sobre você...'}),
            'instituicao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Onde você estuda/trabalha?'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qual seu curso?'}),
        }