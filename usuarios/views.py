from django.contrib.auth.models import User
from posts.models import Postagem 
from .forms import UserUpdateForm, PerfilUpdateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, PerfilUpdateForm
from django.contrib import messages
from .forms import CadastroForm
from django.contrib.auth import login

def ver_perfil(request, username):
    dono_perfil = get_object_or_404(User, username=username)
    
    posts = Postagem.objects.filter(autor=dono_perfil).order_by('-data_publicacao')
    
    return render(request, 'usuarios/perfil.html', {
        'dono_perfil': dono_perfil,
        'posts': posts
    })

 

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PerfilUpdateForm(request.POST, instance=request.user.perfil)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save() 
            p_form.save() 
            return redirect('ver_perfil', username=request.user.username)
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PerfilUpdateForm(instance=request.user.perfil)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'usuarios/editar_perfil.html', context)

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST) 
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            messages.success(request, f'Bem-vindo, {user.username}!')
            
            return redirect('feed') 
    else:
        form = CadastroForm()
    
    

    return render(request, 'registration/cadastro.html', {'form': form})