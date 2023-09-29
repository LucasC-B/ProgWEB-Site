from django.shortcuts import render, redirect, get_object_or_404
from filmes.forms import InsereFilmeForm, AtualizaFilmeForm
from usuarios.models import Usuario
from django.contrib import messages
from filmes.models import Filme

def postaFilmeView(request):
    context ={}
    
    user = request.user
    if not user.is_authenticated:
        return redirect('deveAutenticar')
    
    form = InsereFilmeForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        objeto = form.save(commit=False)
        usuario = Usuario.objects.filter(email=user.email).first()
        objeto.usuario = usuario
        objeto.save()
        form = InsereFilmeForm()
        messages.success(request, 'Filme adicionado!')
        return redirect('home')
    
    context['form'] = form
    return render(request, "filmes/postaFilme.html", context)

def apagaFilmeView(request, slug):
    context = {}
    filme = get_object_or_404(Filme, slug=slug)
    
    if request.POST:
        filme.delete()
        messages.success(request, 'Filme retirado!')
        return redirect('home')
    
    context['filme'] = filme
    return render(request, 'filmes/apagaFilme.html', context)

def editaFilmeView(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('deveAutenticar')
    filme = get_object_or_404(Filme, slug=slug)
    if request.POST:
        form = AtualizaFilmeForm(request.POST or None, request.FILES or 
                                 None, instance=filme)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.save()
            messages.success(request, 'Informações do filme atualizadas!')
            filme = objeto
            return redirect('home')
        
    form = AtualizaFilmeForm(
        initial= {
            "titulo": filme.titulo,
            "nacionalidade": filme.nacionalidade,
            "ano": filme.ano,
            "sinopse": filme.sinopse,
            "diretor": filme.diretor,
            "nota": filme.nota,
            "review": filme.review,
            "visto": filme.visto
        }
    )
    context['form'] = form
    return render(request, 'filmes/editaFilme.html', context)
            

def detalhaFilmeView(request,slug):
    contexto={}
    filme=get_object_or_404(Filme,slug=slug)
    contexto['filme']=filme
    return render(request, 'filmes/detalhaFilme.html' ,contexto)