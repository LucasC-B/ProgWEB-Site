from django.shortcuts import render
from usuarios.models import Usuario
from django.views.generic.base import View

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        contexto = { 'usuarios': usuarios, }
        return render(
            request,
            'usuarios/listaUsuarios.html',
            contexto)