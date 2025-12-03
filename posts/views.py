from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Postagem, Comentario
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ComentarioForm

def index(request):
    return HttpResponse("<h1> Bem vindo a rota de posts</h1>")

def feed(request):
    posts_list = Postagem.objects.all().order_by('-data_publicacao')
    
    paginator = Paginator(posts_list, 5) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('HX-Request'):
        return render(request, 'posts/partials/lista_posts.html', {'page_obj': page_obj})

    return render(request, 'posts/feed.html', {'page_obj': page_obj})


def post_detail(request, pk):
    post = get_object_or_404(Postagem, pk=pk)
    comentarios = post.comentarios.all().order_by('-data_comentario') 
    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comentarios': comentarios
    })


def curtir_post(request, pk):
    post = get_object_or_404(Postagem, pk=pk)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user) 
    else:
        post.likes.add(request.user)    
        
    return render(request, 'posts/partials/botao_curtida.html', {'post': post})


def post_detail(request, pk):
    post = get_object_or_404(Postagem, pk=pk)
    comentarios = post.comentarios.all().order_by('-data_comentario') 
    
    form = ComentarioForm()
    
    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form,
    })

@login_required # Só quem tá logado pode comentar
def adicionar_comentario(request, pk):
    post = get_object_or_404(Postagem, pk=pk)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.postagem = post
            comentario.autor = request.user

            comentario.save()
            
    return redirect('post_detail', pk=post.pk)

@login_required
def deletar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    post_id = comentario.postagem.pk 
    

    if request.user == comentario.autor or request.user == comentario.postagem.autor:
        comentario.delete()
    

    return redirect('post_detail', pk=post_id)