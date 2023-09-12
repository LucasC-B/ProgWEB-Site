from django.db import models

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)

    nome = models.CharField(help_text='Entre o nome', 
                            max_length=100)
    
    idade = models.IntegerField(help_text='Entre a idade')

    salario = models.DecimalField(help_text='Entre o salario',
                                  decimal_places=2, 
                                  max_digits=8)
    
    email = models.EmailField(help_text='Informe o email',
                              max_length=254)
    
    telefone = models.CharField(help_text='Telefone com DDD e DDI', 
                                max_length=20)
    
    dtNasc = models.DateField(help_text='Nascimento no formato DD/MM/AAAA',
                              verbose_name='Data de nascimento')
    
    def __str__(self):
        return self.nome
