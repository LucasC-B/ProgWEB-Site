from django.urls import path

from filmes.views import (
    postaFilmeView,
    editaFilmeView,
    apagaFilmeView,
    
)

app_name = 'filmes'

urlpatterns = [
    path('posta/', postaFilmeView, name = "posta" ),
    path('<slug>/edita',editaFilmeView, name = "edita" ),
    path('<slug>/delete', apagaFilmeView, name ="apaga" ),
    
]
