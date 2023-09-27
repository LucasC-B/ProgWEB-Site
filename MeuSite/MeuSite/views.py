from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from filmes.models import Filme
from operator import attrgetter
from django.conf import settings
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

def visualizaTelaHome(request):

    contexto = {}

    filme = sorted(Filme.objects.all(usuario=request.user), attrgetter('titulo'), reverse=True)
    contexto['filmes'] = filme

    pagina = request.GET.get("pagina",1)
    filmesEmPaginas = Paginator(filme, settings.FILMES_PER_PAGE)

    try:
        filme = filmesEmPaginas.page(pagina)
    except PageNotAnInteger:
        filme = filmesEmPaginas.page(settings.FILMES_PER_PAGE)
    except:
        filme = filmesEmPaginas.page(filmesEmPaginas.num_pages)

    contexto['filmes'] = filme
    return render(request,'home/home.html', contexto)