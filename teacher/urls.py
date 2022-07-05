from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home, name='Home'),
    path('criar_lista/', views.criarLista, name='criarLista'),
    path('historico_de_listas/', views.listarListas, name='listarListas'),
    path('excluir/<int:Lista_presenca_id>/', views.excluirLista, name='excluirLista'),
    path('opcoes_lista/<int:Lista_presenca_id>/', views.opcoesLista, name='excluirLista'),
    path('adicionar_estudante/<int:Lista_presenca_id>/', views.adicionarEstudante, name='adicionarEstudante'),
    path('alunos_presentes/<int:Lista_presenca_id>/', views.listarAlunos, name='listarAlunos'),
    path('salvar_lista/<int:Lista_presenca_id>/', views.salvarLista, name='salvarLista'),

]