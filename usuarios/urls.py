from django.urls import path

from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/<str:username>/', views.ver_perfil, name='ver_perfil'),
    path('editar/', views.editar_perfil, name='editar_perfil'),
]