from django.urls.conf import path
from usuarios import views

app_name = "usuarios"

urlpatterns = [
    path('cria/', views.UsuarioCreateView.as_view(),
        name='cria-usuarios'),
    path('lista/', views.UsuarioListView.as_view(),
        name='lista-usuarios'),
    path('atualiza/<int:pk>', views.UsuarioUpdateView.as_view(), 
         name='atualiza-usuario'),
    path('apaga/<int:pk>/', views.UsuarioDeleteView.as_view(), 
         name='apaga-usuario'),
    path('', views.UsuarioListView.as_view(),
        name='home-usuarios'),
]