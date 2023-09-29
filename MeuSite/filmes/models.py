from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

def localiza(instance,filename):
    
    path = 'filme/{usuario_id}/{titulo}-{filename}'.format(
        usuario_id=str(instance.usuario.id), titulo = str(instance.titulo), filename = filename
        )
    
    return path

class Filme(models.Model):
    titulo = models.CharField(help_text='Digite o titulo do filme', 
                              max_length=50, null=False, blank=False)
    nacionalidade = models.CharField(help_text='Digite a nacionalidade do filme', 
                              max_length=50, null=False, blank=False)
    ano = models.CharField(help_text='Digite o ano de lancamento do filme', 
                              max_length=50, null=False, blank=False)
    sinopse = models.CharField(help_text='Digite o titulo do filme', 
                              max_length=200, null=True, blank=True)
    diretor = models.CharField(help_text='Digite o nome do diretor', 
                              max_length=50, null=False, blank=False)
    genero = models.CharField(help_text='Digite o genero do filme', 
                              max_length=50, null=False, blank=False)
    nota = models.CharField(help_text='Digite a nota que avalia o filme', 
                              max_length=50, null=True, blank=True)
    review = models.CharField(help_text='Digite um breve review do filme', 
                              max_length=200, null=True, blank=True)
    visto = models.BooleanField(default=False)
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.titulo
    
@receiver(post_delete, sender=Filme)
def salva_recebe_filme(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.usuario.username + "-" + instance.titulo)

pre_save.connect(salva_recebe_filme, sender=Filme)
    
