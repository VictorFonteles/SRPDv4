from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Lista_presenca, Estudante_ad
from . forms import ListForm, FormEstudante
from django.contrib.auth.decorators import login_required


@login_required
def Home(request): 
    if Lista_presenca.objects.all():
        lista = Lista_presenca.objects.last()     
        if lista.condicao == '0':
            return render(request, 'teacher/home.html')
        else :
            context = {
            "lista": lista
            }
            return render(request, 'teacher/homeListaAberta.html/', context)          
    else :
        return render(request, 'teacher/home.html')

@login_required
def criarLista(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
             lista = form.save()
             lista.condicao = 'a'
             lista.save()
             context = {
             "lista": lista
             }
             return HttpResponseRedirect('/teacher/home/', context)
    else:
        form = ListForm()
        context={'form': form}
        return render(request, 'teacher/criarLista.html', context)

@login_required
def adicionarEstudante(request, Lista_presenca_id):
    if request.method == "POST":
        form = FormEstudante(request.POST)
        if form.is_valid():  
            estudante = form.save()           
            return HttpResponseRedirect('/teacher/home/')
    else :
        form = FormEstudante()
        context={'form': form}
        return render(request, 'teacher/adicionarEstudante.html', context)

@login_required
def opcoesLista(request, Lista_presenca_id):
    if Lista_presenca.objects.all():
        lista = Lista_presenca.objects.get(pk=Lista_presenca_id)
        if lista.condicao == '0':
            return render(request, 'teacher/home.html')
        else:
            context = {
            "lista": lista
            }
            return render(request, 'teacher/opcoesLista.html', context)         
    else :
        return render(request, 'teacher/home.html')

@login_required
def salvarLista(request, Lista_presenca_id):
    lista = Lista_presenca.objects.get(pk=Lista_presenca_id)
    lista.condicao = '0'
    lista.save()
    listas = Lista_presenca.objects.all()
    return HttpResponseRedirect('/teacher/home/')
    

@login_required
def listarListas(request):
    listas = Lista_presenca.objects.all()
    context = {
        "listas": listas
    }
    return render(request, 'teacher/historico.html', context)


@login_required
def listarAlunos(request, Lista_presenca_id):
    assinantes = Estudante_ad.objects.filter(identificador_lista=Lista_presenca_id)
    context = {
        'assinantes': assinantes
    }
    return render(request, 'teacher/AlunosPresentes.html', context)

@login_required
def baixarLista(request):
    return HttpResponse("Baixar lista em pdf")

@login_required
def baixarTodasListas(request):
    return HttpResponse("Baixar todas as listas")

@login_required
def excluirLista(request, Lista_presenca_id):
    Lista_presenca.objects.get(pk=Lista_presenca_id).delete()
    return HttpResponseRedirect("/teacher/historico_de_listas/")





