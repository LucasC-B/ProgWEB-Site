from django.urls.conf import path
from usuarios import views

app_name = "usuarios"

urlpatterns = [
    path('cria/', views.UsuarioCreateView.as_view(),
        name='cria-usuarios'),
    path('lista/', views.UsuarioListView.as_view(),
        name='lista-usuarios'),
    path('', views.UsuarioListView.as_view(),
        name='home-usuarios'),
]