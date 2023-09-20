from usuarios.models import Usuario
from django.views.generic.base import View
from usuarios.forms import UsuarioModel2Form
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

class UsuarioListView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        contexto = { 'usuarios': usuarios, }
        return render(
            request,
            'usuarios/listaUsuarios.html',
            contexto)
    
class UsuarioCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': UsuarioModel2Form, }
        return render(request,
            'usuarios/criaUsuario.html', contexto)
    
    def post(self, request, *args, **kwargs):
        formulario = UsuarioModel2Form(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.save()
            return HttpResponseRedirect(reverse_lazy(
                'usuarios:lista-usuarios'))
        
class UsuarioUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        usuario = Usuario.objects.get(pk=pk)
        formulario = UsuarioModel2Form(instance=usuario)
        context = {'usuario': formulario, }
        return render(request, 'usuarios/atualizaUsuarios.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        usuario = get_object_or_404(Usuario, pk=pk)
        formulario = UsuarioModel2Form(request.POST, instance=usuario)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.save()
            return HttpResponseRedirect(reverse_lazy("usuarios:lista-usuarios"))
        else:
            contexto = {'usuario': formulario, }
            return render(request, 'usuarios/atualizaUsuarios.html', contexto)
        
class UsuarioDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        usuario = Usuario.objects.get(pk=pk)
        contexto = { 'usuario': usuario, }
        return render(request, 'usuarios/apagaUsuarios.html', contexto)
    
    def post(self, request, pk, *args, **kwargs):
        usuario = Usuario.objects.get(pk=pk)
        usuario.delete()
        return HttpResponseRedirect(reverse_lazy("usuarios:lista-usuarios"))
        
        
