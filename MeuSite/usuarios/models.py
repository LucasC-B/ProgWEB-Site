from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)

    nome = models.CharField(help_text='Entre o nome', 
                            max_length=100)
    
    idade = models.IntegerField(help_text='Entre a idade')

    
    email = models.EmailField(help_text='Informe o email',
                              max_length=254)
    
    gender = models.CharField(help='Informe o seu gênero',
                              max_length=15)
    
    
    dtNasc = models.DateField(help_text='Nascimento no formato DD/MM/AAAA',
                              verbose_name='Data de nascimento')
    
    
    def __str__(self):
        return self.nome

