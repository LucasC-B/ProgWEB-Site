from django.shortcuts import render
from usuarios.models import Usuario
from django.views.generic.base import View
from usuarios.forms import UsuarioModel2Form
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