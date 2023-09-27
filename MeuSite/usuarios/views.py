from usuarios.models import Usuario
from django.views.generic.base import View
from usuarios.forms import UsuarioModel2Form
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from usuarios.forms import UsuarioRegistraForm
from usuarios.forms import UsuarioAutenticaForm, UsuarioAtualizaForm
from django.contrib import messages
from filmes.forms import Filme
from operator import attrgetter
from django.conf import settings
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
    

def registrarUsuario(request):
    contexto = {}
    if request.POST:
          form = UsuarioModel2Form(request.POST)
          if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            senha_k = form.cleaned_data.get('senha1')
            usuario = authenticate(email=email, password=senha_k)
            login(request, usuario)
            return redirect('home')
          else:
              contexto['registration_form'] = form
    else:
        form = UsuarioRegistraForm
        contexto['registration_form'] = form
    
    return render(request, 'usuarios/registro.html', contexto)


def visualizaLogout(request):
    logout(request)
    messages.success(request, 'Logout feito com sucesso!')
    return redirect('home')


def visualizaLogin(request):
    contexto = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    if request.POST:
            form = UsuarioAutenticaForm(request.POST)
            if form.is_valid():
                email = request.POST['email']
                senha = request.POST['senha']
                user = authenticate(email = email, password=senha)
                
                if user:
                    login(request,user)
                    messages.success(request, 'Login feito com sucesso!') 
                    return redirect("home")
    else:
        form = UsuarioAutenticaForm()
        
    contexto['login_form'] = form
    return render(request, 'usuarios/login.html', contexto)


def visualizaUsuario(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    contexto = {}

    if request.POST:
        form = UsuarioAtualizaForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
				"email": request.POST['email'],
				"nome":request.POST['nome'],
			}
            form.save()
            messages.success(request, 'Conta atualizada com sucesso!')
        else:
            messages.warning(request, 'E-mail ou usuário indisponíveis. Tente novamente.')
    else:
        form = UsuarioAtualizaForm(
            initial={
				"email": request.user.email,
				"nome": request.user.username,
			}
        )

    contexto['usuario_form'] = form
    filme = sorted(Filme.objects.filter(usuario=request.user), key=attrgetter('titulo'), reverse=True)
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
    return render(request,'usuarios/usuario.html', contexto)

def visualizaDeletaUsuario(request):

    if not request.user.is_authenticated:
        return redirect("login")
    
    contexto = {}

    if request.POST:
        email = request.POST['email']
        senha = request.POST['senha']

        user = authenticate(email = request.user.email, password = senha)

        if user:
            user.delete()
            messages.success(request, 'Conta deletada com sucesso!')
            return redirect("home")
        else:
            messages.warning(request, 'Usuário ou senha incorretos. Tente novamente.')

    return render(request, 'usuarios/deletaUsuario.html', contexto)


def visualizaAutentica(request):
	return render(request,"usuarios/deveAutenticar.html",{})