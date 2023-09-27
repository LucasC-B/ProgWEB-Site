from django import forms
from usuarios.models import Usuario
from django.contrib.auth import UserCreationForm
from django.contrib.auth import authenticate
from typing import Any


class UsuarioRegistraForm(UserCreationForm):

    email = forms.EmailField(max_length=60, help_text="Obrigatório. Entre com o seu email")

    class Meta:
        model = Usuario
        fields = ('email', 'nome', 'senha1', 'senha2')

class UsuarioAutenticaForm(forms.ModelForm):
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email', 'senha')

    def analisa(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            senha = self.cleaned_data['senha']
            if not authenticate(email=email, password = senha):
                raise forms.ValidationError("Login Inválido")
            
class UsuarioAtualizaForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('email','nome')

    def analisa_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                usuario = Usuario.objects.exclude(pk=self.instance.pk).get(email=email)
            except Usuario.DoesNotExist:
                 return email
            raise forms.ValidationError('Email "%s" já sendo utilizado.' % email)
        
    def analisa_nome(self):
        if self.is_valid():
            nome = self.cleaned_data['nome']
            try:
                usuario = Usuario.objects.exclude(pk=self.instance.pk).get(username=nome)
            except Usuario.DoesNotExist:
                 return nome
            raise forms.ValidationError('Nome "%s" já sendo utilizado.' % nome)
        