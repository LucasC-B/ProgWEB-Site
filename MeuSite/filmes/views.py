from django.shortcuts import render, redirect, get_object_or_404
from filmes.forms import InsereFilmeForm, AtualizaFilmeForm
from usuarios.models import Usuario
from django.contrib import messages
from filmes.models import Filme

def postaFilmeView(request):
    context ={}
    
    usuario = request.usuario
    if not usuario.is_authenticated:
        return redirect('deveAutenticar.html')
    
    form = InsereFilmeForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        objeto = form.save(commit=False)
        usuario = Usuario.objects.filter(email=usuario.email).first()
        objeto.usuario = usuario
        objeto.save()
        form = InsereFilmeForm()
        messages.success(request, 'Filme adicionado!')
        return redirect('home')
    
    context['form'] = form
    return render(request, "filmes/postaFilme.html")

def apagaFilmeView(request, slug):
    context = {}
    filme = get_object_or_404(Filme, slug=slug)
    
    if request.POST:
        filme.delete()
        messages.success(request, 'Filme retirado!')
        return redirect('home')
    
    context['filme'] = filme
    return render(request, 'filmes/apagaFilme.html')

def editaFilmeView(request, slug):
    context = {}
    
    usuario = request.usuario
    if not usuario.is_authenticated:
        return redirect('deveAutenticar.html')
    
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
            inicial= {
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
            
        
    