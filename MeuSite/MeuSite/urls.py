"""
URL configuration for MeuSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from usuarios import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls.base import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from MeuSite.views import visualizaTelaHome
from usuarios.views import (
    registrarUsuario,
    visualizaLogout,
    visualizaLogin,
    visualizaUsuario,
    visualizaDeletaUsuario,
    visualizaAutentica
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', visualizaTelaHome, name='home'),
    path('registro/', registrarUsuario, name = "registro"),
    path('login/', visualizaLogin, name = "login"),
    path('logout/', visualizaLogout, name = "logout"),
    path('usuario/', visualizaUsuario, name = "usuario"),
    path('deleta_usuario/', visualizaDeletaUsuario, name = "deleta_usuario"),
    path('filme/', include('filmes.urls', 'filmes')),
    path('must_authenticate/', visualizaAutentica, name = "deveAutenticar"),
    path('muda_senha/done/', auth_views.PasswordChangeView.as_view(template_name='registro/password_change_done.html'), 
         name='password_change_done'),
    path('muda_senha/', auth_views.PasswordChangeView.as_view(template_name='registro/mudaSenha.html'), 
         name='muda_senha'),
    path('recupera_senha/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registro/recuperaSenhaDone.html'), 
         name='recupera_senha_done'),
    path('recupera_senha/', auth_views.PasswordResetView.as_view(), 
         name='recupera_senha'),    
    path('recupera/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), 
         name='recupera_confirma'),
    path('recupera/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registro/recuperaCompleto.html'), 
         name='recupera_completa'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
