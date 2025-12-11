from django.urls import path

from . import views

urlpatterns = [
    path("", views.feed, name="feed"),
    path('post/novo/', views.criar_post, name='criar_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/curtir/', views.curtir_post, name='curtir_post'),
    path('post/<int:pk>/comentar/', views.adicionar_comentario, name='adicionar_comentario'),
    path('comentario/<int:pk>/delete/', views.deletar_comentario, name='deletar_comentario'),
]